// Import the Express module
const express = require('express');

// Create an instance of an Express application
const app = express();

// Define a simple route
app.get('/', (req, res) => {
    res.send('Hi i am Muhammad Mohsin');
});

// Define the port the app will listen on
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
