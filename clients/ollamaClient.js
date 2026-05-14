const fetch = require('node-fetch');

async function getEmbeddingFromOllama(prompt) {
  const response = await fetch('http://localhost:11434/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'llama3', prompt })
  });

  const result = await response.json();
  return result.embedding; // Adjust if your Ollama model returns differently
}

module.exports = { getEmbeddingFromOllama };
