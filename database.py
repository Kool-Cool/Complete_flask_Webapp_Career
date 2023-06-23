import sqlalchemy 
from sqlalchemy import create_engine


print(sqlalchemy.__version__)


# For establishing connections between mysql and sqlalchemy
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

engine = create_engine("mysql+pymysql://2zrrxqiz2xmqw0xrig7z:pscale_pw_bcakfQWgKZBZvnbkBzjx9PMSXIU79pES8BYa1gpKsjA@aws.connect.psdb.cloud/dbname?charset=utf8mb4")