const express = require('express');
const bodyParser = require('body-parser');
const ingestRoute = require('./routes/ingest');

const app = express();
app.use(bodyParser.json());

app.use('/ingest', ingestRoute);
app.get('/status', (req, res) => {
  res.send('Backend is online!');
});

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
