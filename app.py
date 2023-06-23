from flask import Flask 
from flask import render_template , jsonify
from database import engine
from sqlalchemy import text



app = Flask(__name__)




def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for row in result.all():
      jobs.append(row._aasdict())

    return jobs
  

@app.route("/") #html route
def hello_word():
  jobs = load_jobs_from_db()
  return render_template("home.html",jobs_to_show = jobs)
  

@app.route("/jobs") #API route
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
