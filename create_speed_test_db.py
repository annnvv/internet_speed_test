## Identify() info: https://docs.sqlalchemy.org/en/14/core/defaults.html#identity-ddl
##av.note: not sure whether I want the JSON column to be mutuable (without Mutable Dict, the ORM does not recognize in place mutations)
##JSONB info: https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/

import yaml
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Identity,
    Integer,
    Float,
    DateTime,
)
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB

## Create engine
with open("database/config.yaml", "r") as f:
    config = yaml.safe_load(f)

engine = create_engine(
    f"postgresql+psycopg2://{config['db']['user_name']}:{config['db']['password']}@{config['db']['host_name']}:{config['db']['port']}/{config['db']['db_name']}",
    echo=True,
)

## Define table
Base = declarative_base()


class SpeedTest(Base):
    __tablename__ = "speed_test"

    speed_test_id = Column(
        Integer,
        Identity(start=1, increment=1, always=True, cycle=True),
        primary_key=True,
        unique=True,
        nullable=False,
    )
    timestamp = Column(DateTime)
    download_speed_Mb = Column(Float)
    upload_speed_Mb = Column(Float)
    bytes_sent = Column(Integer)
    bytes_received = Column(Integer)
    ping = Column(Float)
    server_info = Column(MutableDict.as_mutable(JSONB))


# Base.metadata.drop_all(engine)
## Create table
Base.metadata.create_all(engine)
