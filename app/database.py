from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

DB_CONNECTION_URL = 'postgresql://postgres:C00ljoe.@localhost/fastapi-practice'

engine = create_engine(DB_CONNECTION_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi-practice', user='postgres', password='C00ljoe.', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was established successfully")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
