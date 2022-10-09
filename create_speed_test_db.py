## Identify() info: https://docs.sqlalchemy.org/en/14/core/defaults.html#identity-ddl
##av.note: not sure whether I want the JSON column to be mutuable (without Mutable Dict, the ORM does not recognize in place mutations)
##JSONB info: https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/

import yaml
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
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
meta = MetaData()

## Define table
speed_test = Table(
    "speed_test",
    meta,
    Column(
        "speed_test_id",
        Integer,
        Identity(start=1, increment=1, always=True, cycle=True),
        primary_key=True,
        unique=True,
        nullable=False,
    ),
    Column("timestamp", DateTime),
    Column("download_speed_Mb", Float),
    Column("upload_speed_Mb", Float),
    Column("bytes_sent", Integer),
    Column("bytes_received", Integer),
    Column("ping", Float),
    Column("server_info", MutableDict.as_mutable(JSONB)),
)

## Create table
# meta.drop_all(engine)
meta.create_all(engine)
