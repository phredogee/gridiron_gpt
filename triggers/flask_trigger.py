# flask_trigger.py

from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    subprocess.Popen(["/home/phredo/phredo/my_project/run_pipelines.sh"])
    return "Pipeline triggered", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
