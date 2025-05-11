const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Proxy route
app.post('/generateContent', async (req, res) => {
  const { imageData } = req.body;
  const apiKey = 'AIzaSyB6fX37O4pw8G2o-TWOn5nROIPRHjc07_c'; // User's actual API key
  const prompt = `Identify this whiskey. Provide its name, general composition, and estimated price. Image: ${imageData}`;

  try {
    const response = await fetch('https://gemini.googleapis.com/v1/generateContent', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: "gemini-2.0-flash",
        contents: [
          `Identify this whiskey. Provide its name, general composition, and estimated price. Image:`,
          imageData
        ]
      })
    });

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error('Error forwarding request to Gemini API:', error);
    res.status(500).json({ error: 'Failed to fetch from Gemini API' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Proxy server running on http://localhost:${PORT}`);
});
