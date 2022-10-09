# Based on: https://www.educative.io/answers/how-to-detect-internet-speed-using-python
# speedtest-cli is compatible with Python up to 3.7

import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import speedtest
from define_speed_test_class import SpeedTest


def bytes_to_mb(bytes):
    """Convert bytes to megabytes"""

    KB = 1024  # One Kb is 1024 bytes
    MB = KB * 1024  # One Mb is 1024 Kb
    return bytes / MB


## EXTRACT
speed_test = speedtest.Speedtest(secure=True)
speed_test.get_best_server()

speed_test.download()
speed_test.upload()

results = speed_test.results.dict()

## TRANSFORM
results["download_speed_Mb"] = bytes_to_mb(results["download"])
results["upload_speed_Mb"] = bytes_to_mb(results["upload"])

del (
    results["client"],
    results["share"],
    results["download"],
    results["upload"],
)  ## remove from dictionary, do not need this info


## LOAD
with open("database/config.yaml", "r") as f:
    config = yaml.safe_load(f)

engine = create_engine(
    f"postgresql+psycopg2://{config['db']['user_name']}:{config['db']['password']}@{config['db']['host_name']}:{config['db']['port']}/{config['db']['db_name']}",
    echo=True,
)

Session = sessionmaker(bind=engine)
s = Session()

data = SpeedTest(**results)

s.add(data)

s.commit()
s.close()
