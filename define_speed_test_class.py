from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

## Define table
Base = declarative_base()


class SpeedTest(Base):
    __tablename__ = "speed_test"

    speed_test_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    timestamp = Column(DateTime)
    download_speed_mb = Column(Float)
    upload_speed_mb = Column(Float)
    bytes_sent = Column(Integer)
    bytes_received = Column(Integer)
    ping = Column(Float)
