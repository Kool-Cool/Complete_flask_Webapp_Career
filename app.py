from flask import Flask 
from flask import render_template , jsonify , request
from database import load_jobs_from_db , load_job_from_db_of_id , add_application_to_db




app = Flask(__name__)





  

@app.route("/") #html route
def hello_word():
  jobs = load_jobs_from_db()
  return render_template("home.html",jobs_to_show = jobs)
  

@app.route("/api/jobs") #API route
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)



@app.route("/job/<id>") #Dynamic route # Kinda REST API (GOES THROUGH DATA AND RETURN JSON FILE)
def show_job(id):
  job = load_job_from_db_of_id(id)
  if not job:
    return "Not Found",404
  return render_template("jobpage.html",job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  # data = request.args # .args get data from url
  data = request.form
  job = load_job_from_db_of_id(id)
  add_application_to_db(id , data)
  return render_template("application_submitted.html",application=data , job=job)


@app.route("/api/job/<id>") #Individual JOB listing
def show_job_json(id):
  job = load_job_from_db_of_id(id)
  return jsonify(job)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/connect")
def connect():
    return render_template("connect.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
