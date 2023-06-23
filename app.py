from flask import Flask 
from flask import render_template , jsonify , request
from database import load_jobs_from_db , load_job_from_db_of_id




app = Flask(__name__)





  

@app.route("/") #html route
def hello_word():
  jobs = load_jobs_from_db()
  return render_template("home.html",jobs_to_show = jobs)
  

@app.route("/jobs") #API route
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
  
  
  return jsonify(data)





if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
