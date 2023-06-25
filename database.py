
from sqlalchemy import create_engine
from sqlalchemy import text
import os
# print(sqlalchemy.__version__)

# NOTE
# MAKE sure you have saved data of Connection strings from PLanetScale




# For establishing connections between mysql and sqlalchemy
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
db_connection_string = str(os.environ["DB_CONNECTION_STRING"])

engine = create_engine(db_connection_string ,
                      connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      }
                      )


with engine.connect() as conn:
  db_query = "select * from jobs"
  result = conn.execute(text(db_query))

  result_dicts = []

for row in result.all():
  result_dicts.append(row._asdict())

# print(result_dicts)


# Helper Function

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs


def load_job_from_db_of_id(id):
  with engine.connect() as conn:
    query = f"SELECT * FROM jobs WHERE id = {id} "
    result = conn.execute(text(query))
    rows = result.all()
    if len(rows)== 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id ,application_info ):
  with engine.connect() as conn:
    query = text(f"INSERT INTO applications (job_id , full_name , email ,linkedin_url , work_experience , resume_url)  VALUES ({job_id} ,'{application_info['full_name']}' ,'{application_info['email']}' ,'{application_info['linkedin_url']}' ,'{application_info['work_experience']}' ,'{application_info['resume_url']}')")

    conn.execute(query)
    
   
    # query =   text(f"INSERT INTO applications (job_id , full_name , email ,linkedin_url , work_experience , resume_url)  VALUES ({job_id} ,{application_info['full_name']} ,{application_info['email']} ,{application_info['linkedin_url']} ,{application_info['work_experience']} ,{application_info['resume_url']})")
# One issue with the code you provided is that the values being inserted into the database are not enclosed in quotation marks. This can cause issues with the SQL statement, especially if the values being inserted contain spaces or special characters. You can try enclosing the values in single quotation marks
