const express = require('express');
const router = express.Router();
const { getEmbeddingFromOllama } = require('../clients/ollamaClient');
const { createVerbaEntry } = require('../clients/weaviateClient');

router.post('/', async (req, res) => {
  const { text, metadata } = req.body;
  try {
    const vector = await getEmbeddingFromOllama(text);
    const result = await createVerbaEntry(text, metadata, vector);
    res.status(200).json(result);
  } catch (error) {
    res.status(500).json({ error: 'Ingestion failed', details: error.message });
  }
});

module.exports = router;
