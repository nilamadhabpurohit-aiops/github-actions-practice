from flask import Flask, render_template, jsonify
import os
import socket
import datetime


app = Flask(__name__)

VERSION = os.getenv("GITHUB_SHA", "local")
IMAGE = os.getenv("IMAGE", "github-actions-capstone")


def check_service(name):
    try:
        return "Healthy"
    except Exception:
        return "Down"


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/health")
def health():

    return jsonify(
        {
            "status": "healthy",
            "time": str(datetime.datetime.now()),
            "host": socket.gethostname(),
        }
    )


@app.route("/metrics")
def metrics():

    data = {
        "service": "Payment API",
        "version": VERSION[:7],
        "image": IMAGE,
        "environment": "production",
        "pipeline": "Passing",
        "security": "Scanned",
        "time": str(datetime.datetime.now()),
        "host": socket.gethostname(),
        "python": os.sys.version.split()[0],
    }

    return jsonify(data)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)