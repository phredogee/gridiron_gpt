from flask import Flask, request, jsonify
from pipelines.ranking_pipeline import run_pipeline_logic  # if you want to modularize

app = Flask(__name__)

@app.route("/run_pipeline", methods=["POST"])
def run_pipeline():
    data = request.get_json()
    print("Received trigger:", data)

    # Call your pipeline logic here
    result = run_pipeline_logic(data)  # or just placeholder logic

    return jsonify({"status": "success", "result": result}), 200

if __name__ == "__main__":
    app.run(port=5000)
