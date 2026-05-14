const express = require('express');
const app = express();
const PORT = 8000;

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from Verba backend!' });
});

app.listen(PORT, () => {
  console.log(`Backend listening on port ${PORT}`);
});
