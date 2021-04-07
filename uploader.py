import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


def Uploader(path):
    path = Path(path)
    dir_list = sorted(list(path.iterdir()), key=lambda x: x.stat().st_ctime, reverse=True)

    crm_file = pd.read_csv(dir_list[0].absolute())
    engine = create_engine('mysql://leo:1q2w3e4r@10.1.1.105/crm')
    sql = 'DROP TABLE crm.crm'
    engine.execute(sql)
    crm_file.to_sql('crm', con=engine)

    dir_list[0].unlink(missing_ok=True)


if __name__ == "__main__":
    Uploader('C:\\Users\\Server\\Downloads\\')
