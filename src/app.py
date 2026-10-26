
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read an environment variable
app_env = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    print(f"A visitor opened the homepage! Current environment: {app_env}", flush=True)

    return jsonify(
        message="Hello from my Python Flask app!",
        environment=app_env,
        tip="Set APP_ENV=production to change this response."
    )

if __name__ == "__main__":
    print(f"Starting Flask app in {app_env} mode!", flush=True)
    app.run(host="0.0.0.0", port=5000)
