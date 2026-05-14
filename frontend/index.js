fetch('http://localhost:8000/api/data')
  .then(res => res.json())
  .then(data => {
    document.getElementById('output').textContent = data.message;
  })
  .catch(err => {
    console.error('Fetch error:', err);
    document.getElementById('output').textContent = 'Error reaching backend.';
  });
