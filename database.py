from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://kdcww2ytq4d5m6r05dm6:pscale_pw_h4lF1DGMIEw0htHorgcQID4Yn8TfU4XLvBuL8E63gZs@aws.connect.psdb.cloud/jobnavcareers?charset=utf8mb4"
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
