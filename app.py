from flask import Flask, request, jsonify
import google.generativeai as genai
import io
import base64
import json
from flask_cors import CORS
import requests
import PIL.Image
import re # Import the regular expression module
import binascii # Import binascii for base64 errors
import traceback # Import traceback for detailed error logging

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # Enable CORS for specific origin

# Consider loading API key from environment variables for security
API_KEY = "AIzaSyB6fX37O4pw8G2o-TWOn5nROIPRHjc07_c"  # User's actual API key

# Configure the genai library with the API key
# This method is recommended by the traceback for proper authentication
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring Google Generative AI API: {e}")
    # Handle configuration error if necessary

# Initialize the Generative Model outside the request function for efficiency
# This avoids re-initializing the model on every request
model = None # Initialize model variable
try:
    # Use a model name that supports multimodal input (text and image)
    # "gemini-pro-vision" or "gemini-flash-vision" are suitable options.
    # Let's stick with "gemini-2.0-flash" as you specified, assuming it supports vision in your setup.
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    # A simple test to ensure the model is accessible after initialization
    # This might not be strictly necessary but can help catch immediate issues
    # model.count_tokens("test")
except Exception as e:
    print(f"Error initializing GenerativeModel: {e}")
    # Depending on your application, you might want to handle this more gracefully,
    # perhaps by returning an error response for all subsequent requests.
    model = None # Set model to None if initialization fails

@app.route('/generateContent', methods=['POST'])
def generate_content():
    # Check if the model was successfully initialized
    if model is None:
         print("Model not initialized, returning 500.")
         return jsonify({"error": "AI model failed to initialize on the server. Please check server logs for configuration or initialization errors."}), 500

    try:
        data = request.json
        image_data = data.get('image')

        if not image_data:
            print("Missing image data in request.")
            return jsonify({"error": "Missing 'image' field in request payload"}), 400

        # Check if the image_data is a data URI and remove the prefix if present
        # A common data URI pattern for images is data:image/<type>;base64,...
        data_uri_pattern = re.compile(r'^data:image/[a-zA-Z]+;base64,')
        if data_uri_pattern.match(image_data):
            image_data = data_uri_pattern.sub('', image_data)

        # Decode the base64 string
        image_bytes = base64.b64decode(image_data)

        # Open the image using PIL
        image = PIL.Image.open(io.BytesIO(image_bytes))

        # Prepare the prompt
        # Note: The image is passed separately, not within the prompt string
        prompt = '''
        Identify this whiskey. Provide its name, general composition, and estimated price.
        Return the information in JSON format.
        '''

        # Generate content using Gemini
        # Use the initialized model instance
        response = model.generate_content(
            contents=[prompt, image] # Pass prompt and image as separate items
        )

        # Parse the response
        # Remove markdown code block formatting if present
        # Check if response.text is not None before calling replace
        ocr_result = response.text
        if ocr_result is not None:
             ocr_result = ocr_result.replace('```json\n', '').replace('```', '').strip()
        else:
             # Handle cases where response.text might be None or empty
             print("Warning: response.text is None or empty from the model.")
             return jsonify({"error": "Received empty or invalid response from the AI model"}), 500


        # Load the JSON data
        try:
            data = json.loads(ocr_result)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Response text was: {ocr_result}")
            return jsonify({"error": "Failed to parse JSON response from model", "details": str(e), "raw_response": ocr_result}), 500


        return jsonify(data)

    except requests.exceptions.RequestException as e:
        # Handle potential issues with the API request itself
        print(f"API Request Error occurred: {e}")
        traceback.print_exc() # Print full traceback to server logs
        return jsonify({"error": "Error communicating with the AI model", "details": str(e)}), 500
    except binascii.Error as e:
        # Handle base64 decoding errors specifically using binascii.Error
        print(f"Base64 Decoding Error: {e}")
        traceback.print_exc() # Print full traceback to server logs
        return jsonify({"error": "Failed to decode base64 image data (Incorrect padding or format)", "details": str(e)}), 400
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc() # Print full traceback to server logs
        return jsonify({"error": "An internal server error occurred", "details": str(e)}), 500


if __name__ == '__main__':
    # In a production environment, set debug=False
    app.run(debug=True)
