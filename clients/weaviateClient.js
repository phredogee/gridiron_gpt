const fetch = require('node-fetch');

async function createVerbaEntry(text, metadata, vector) {
  const payload = {
    class: 'VerbaEntry',
    properties: { text, metadata },
    vector
  };

  const response = await fetch('http://localhost:8080/v1/objects', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  return response.json();
}

module.exports = { createVerbaEntry };
