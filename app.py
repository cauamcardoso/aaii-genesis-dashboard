"""
AAII × DOE Genesis Mission — Faculty Expertise Intelligence Dashboard
Flask application for deployment on Render.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
