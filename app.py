import os

from flask import Flask, render_template, request, send_from_directory

from planner_utils import generate_ai_checklists

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form.get("goal")
    hours = request.form.get("hours")
    markdown = generate_ai_checklists(goal, hours)
    return {"markdown": markdown}


@app.route("/sw.js")
def serve_sw():
    return send_from_directory("static", "sw.js")


if __name__ == "__main__":
    # Listens on 0.0.0.0 to make it easier for containerization/GCP later
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001)),
        debug=os.getenv("FLASK_DEBUG") == "1",
    )
