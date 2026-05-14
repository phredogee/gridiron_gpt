# Clean up stale Python bytecode
find . -name "__pycache__" -type d -exec rm -r {} +
find . -name "*.pyc" -delete
