const express = require('express');
const bodyParser = require('body-parser');
const ingestRoute = require('./routes/ingest');

const app = express();
app.use(bodyParser.json());

// Mount the ingest route
app.use('/ingest', ingestRoute);

// Optional: health check route
app.get('/status', (req, res) => {
  res.send('Backend is online!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server listening on port ${PORT}`);
});
