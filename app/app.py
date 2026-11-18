from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Cloud Deployment Pipeline - Stage 1 Live!</h1>
    <p>Served from AWS EC2 Host: <b>{hostname}</b></p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
