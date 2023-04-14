from flask import Flask, render_template, jsonify
from database import load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_job_from_db()
  return render_template('Home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
