const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const PORT = 8000;

app.use(bodyParser.json());

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from Verba backend!' });
});

app.post('/api/query', async (req, res) => {
  const { input } = req.body;

  try {
    // Step 1: Query Ollama
    const ollamaResponse = await axios.post('http://localhost:11434/api/generate', {
      model: 'llama2',
      prompt: input
    });

    const generatedText = ollamaResponse.data.response;

    // Step 2: Query Weaviate
    const weaviateQuery = {
      query: `
        {
          Get {
            Documents(where: {
              operator: NearText,
              valueText: "${generatedText}"
            }) {
              title
              content
              relevance
            }
          }
        }
      `
    };

    const weaviateResponse = await axios.post('http://localhost:8080/v1/graphql', weaviateQuery);
    const results = weaviateResponse.data.data.Get.Documents;

    res.json({
      query: input,
      response: generatedText,
      results
    });

  } catch (err) {
    console.error('Semantic route failed:', err.message);
    res.status(500).json({ error: 'Semantic pipeline error.' });
  }
});

app.listen(PORT, () => {
  console.log(`Backend listening on port ${PORT}`);
});const express = require('express');
const app = express();
const PORT = 8000;

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from Verba backend!' });
});

app.listen(PORT, () => {
  console.log(`Backend listening on port ${PORT}`);
});
