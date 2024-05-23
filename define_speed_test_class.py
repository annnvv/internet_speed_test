from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Identity,
    Integer,
    Float,
    DateTime,
)
from sqlalchemy.ext.mutable import MutableDict

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
