from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = "GitOps Application Delivery"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "status": "running",
        "version": APP_VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/status")
def deployment_status():
    return jsonify({
        "application": APP_NAME,
        "deployment_status": "successful",
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
