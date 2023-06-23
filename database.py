
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

print(result_dicts)


# Helper Function

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs