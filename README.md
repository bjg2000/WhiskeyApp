# WhiskeyApp

## Overview
WhiskeyApp is a Progressive Web App (PWA) designed to help users identify whiskeys using their mobile device's camera. Users can scan a whiskey bottle or upload an image, and the app will identify the whiskey, provide details such as its name, composition, and estimated price, and allow users to save it to their personal list with notes. The app is fully client-side and stores data locally on the user's device.

## Features
1. **Whiskey Identification**:
   - Uses the Google Gemini API to identify whiskeys from images or barcodes.
   - Provides details such as whiskey name, general composition, and estimated price.

2. **Camera Integration**:
   - Accesses the mobile device's camera to capture images for identification.

3. **User List and Notes**:
   - Allows users to save identified whiskeys to a personal list.
   - Users can add and edit notes for each whiskey.

4. **Local Data Storage**:
   - Stores user data locally using IndexedDB for offline access.

5. **Progressive Web App**:
   - Can be installed on mobile devices for an app-like experience.
   - Works offline for viewing saved whiskeys and notes.

## Technical Details
### Frontend
- **HTML/CSS/JavaScript**:
  - The app's interface is built with responsive design principles for mobile-first usability.
  - JavaScript handles camera access, image capture, and interaction with the Google Gemini API.

- **IndexedDB**:
  - Used for storing user data, including saved whiskeys and notes.

### Backend
- **Flask API (`app.py`)**:
  - Acts as a proxy to securely interact with the Google Gemini API.
  - Handles requests for whiskey identification by forwarding image data and prompts to the Gemini API.

- **Node.js Proxy Server (`proxy-server.js`)**:
  - An alternative backend implementation using Express.js.
  - Provides similar functionality to the Flask API.

### Google Gemini API
- The app uses the Gemini API for multimodal AI capabilities to identify whiskeys and retrieve details.

## How to Run
1. **Install Dependencies**:
   - For Flask backend:
     ```bash
     pip install flask flask-cors requests
     ```
   - For Node.js backend:
     ```bash
     npm install express cors body-parser node-fetch
     ```

2. **Start the Backend**:
   - Flask:
     ```bash
     python app.py
     ```
   - Node.js:
     ```bash
     node proxy-server.js
     ```

3. **Serve the Frontend**:
   - Use a local web server (e.g., Python's `http.server` or a VS Code extension like "Live Server") to serve `index.html`.

4. **Access the App**:
   - Open the app in a browser at `http://localhost:<port>`.

## Future Enhancements
- Add support for barcode scanning.
- Improve error handling and user feedback.
- Enhance offline capabilities with service workers.
- Secure API key usage for production deployment.

## Disclaimer
This app is a prototype and relies on the Google Gemini API for whiskey identification. The estimated price and composition details are based on AI-generated data and may not be accurate.
