
from sqlalchemy import create_engine
from sqlalchemy import text

# print(sqlalchemy.__version__)

# NOTE
# MAKE sure you have saved data of Connection strings from PLanetScale
HOST="aws.connect.psdb.cloud"
USERNAME="bzkm8162ffn8w9l6nayh"
PASSWORD="pscale_pw_AExTSeyjJ4E9zHSGW4npQdJFVjkYCFjMz5bMU9srrkM"
DATABASE="joviancareers"



# For establishing connections between mysql and sqlalchemy
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
db_connection_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4"

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