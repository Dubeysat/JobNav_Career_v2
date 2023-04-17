from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ["DB_CONNECTION_STRING"]
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      print("rows:", row)
      jobs.append(row._asdict())

  return (jobs)


def load_job_from_db(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs where id = :val").bindparams(val=id)
    result2 = conn.execute(query)
    resultall2 = result2.fetchall()
    if len(resultall2) == 0:
      print("No rows found.")
    else:
      for row in resultall2:
        return (row._asdict())
