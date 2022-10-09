# Based on: https://www.educative.io/answers/how-to-detect-internet-speed-using-python
# speedtest-cli is compatible with Python up to 3.7

import yaml
from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from prefect import Task, Flow
import speedtest

from define_speed_test_class import SpeedTest


## EXTRACT function
def get_speed_test_data() -> Dict:
    speed_test = speedtest.Speedtest(secure=True)
    speed_test.get_best_server()

    speed_test.download()
    speed_test.upload()

    dict = speed_test.results.dict()
    return dict

## TRANSFORM function
def bytes_to_mb(bytes):
    """Convert bytes to megabytes"""

    KB = 1024  # One Kb is 1024 bytes
    MB = KB * 1024  # One Mb is 1024 Kb
    return bytes / MB

def transform_speed_test_data(dict: Dict) -> Dict:
    dict["download_speed_Mb"] = bytes_to_mb(dict["download"])
    dict["upload_speed_Mb"] = bytes_to_mb(dict["upload"])

    del (
        dict["client"],
        dict["share"],
        dict["download"],
        dict["upload"],
    )  ## remove from dictionary, do not need this info

    return dict


## LOAD
def etl_pipeline() -> None:
    results = get_speed_test_data()
    results_transformed = transform_speed_test_data(results)

    with open("database/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    engine = create_engine(
        f"postgresql+psycopg2://{config['db']['user_name']}:{config['db']['password']}@{config['db']['host_name']}:{config['db']['port']}/{config['db']['db_name']}",
        echo=True,
    )

    Session = sessionmaker(bind=engine)
    s = Session()

    data = SpeedTest(**results_transformed)

    s.add(data)
    s.commit()
    s.close()
