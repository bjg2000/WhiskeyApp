# WhiskeyApp

## Overview
WhiskeyApp is a Progressive Web App (PWA) designed to help users identify whiskeys using their mobile device's camera. Users can scan a whiskey bottle or upload an image, and the app will identify the whiskey, provide details such as its name, composition, and estimated price, and allow users to save it to their personal list with notes. The app is fully client-side and stores data locally on the user's device.

## Features
1. **Whiskey Identification**:
   - Allows users to upload images for whiskey identification.
   - Provides details such as whiskey name and estimated price.

2. **User List and Notes**:
   - Enables users to save identified whiskeys to a personal list.
   - Users can add and edit notes for each whiskey.

3. **Progressive Web App**:
   - Can be installed on mobile devices for an app-like experience.
   - Works offline for viewing saved whiskeys and notes.

## Technical Details
### Frontend
- **HTML/CSS/JavaScript**:
  - The app's interface is built with responsive design principles for mobile-first usability.
  - JavaScript handles camera access, image capture, and interaction with the Google Gemini API.

- **IndexedDB**:
  - Used for storing user data, including saved whiskeys and notes.


### Google Gemini API
- The app uses the Gemini API for multimodal AI capabilities to identify whiskeys and retrieve details.

## How to Run
1. **Serve the Frontend**:
   - Use a local web server (e.g., Python's `http.server` or a VS Code extension like "Live Server") to serve `index.html`.

2. **Access the App**:
   - Open the app in a browser at `http://localhost:<port>`.

## Future Enhancements
- Add support for barcode scanning.
- Improve error handling and user feedback.
- Enhance offline capabilities with service workers.
- Secure API key usage for production deployment.

## Disclaimer
This app is a prototype and relies on the Google Gemini API for whiskey identification. The estimated price and composition details are based on AI-generated data and may not be accurate.
