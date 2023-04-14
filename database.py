from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://opajh59qe5opkrlox88u:pscale_pw_VcIynkdvydNLoArfU0WQigA5up9giDdiFxgSqcrx10e@aws.connect.psdb.cloud/jobnavcareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_job_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      print("rows:", row)
      jobs.append(row._asdict())

  return (jobs)
