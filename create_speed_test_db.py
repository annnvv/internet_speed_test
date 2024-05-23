## Identify() info: https://docs.sqlalchemy.org/en/14/core/defaults.html#identity-ddl
##av.note: not sure whether I want the JSON column to be mutuable (without Mutable Dict, the ORM does not recognize in place mutations)
##JSONB info: https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/

import yaml
from sqlalchemy import create_engine
from define_speed_test_class import SpeedTest

## Create engine
with open("database/config.yaml", "r") as f:
    config = yaml.safe_load(f)

engine = create_engine(f"sqlite:///{config['db']['db_name']}", echo=True)

SpeedTest.metadata.drop_all(engine)
## Create table
SpeedTest.metadata.create_all(engine)
