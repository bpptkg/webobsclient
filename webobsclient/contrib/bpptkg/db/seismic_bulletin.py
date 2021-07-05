from sqlalchemy import (JSON, Column, DateTime, Float, Integer, String,
                        create_engine)
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class Bulletin(Base):
    """
    BMA bulletin table.

    Reference:
    https://bma.cendana15.com/docs/references/schemas/seismic_bulletin.html#bulletin
    """
    __tablename__ = 'bulletin'

    eventid = Column('eventid', String(100), primary_key=True, index=True)
    eventdate = Column('eventdate', DateTime, index=True)
    eventdate_microsecond = Column(
        'eventdate_microsecond', Integer, index=True, nullable=True)
    number = Column('number', Integer, index=True, nullable=True)
    duration = Column('duration', Float, index=True, nullable=True)
    amplitude = Column('amplitude', String(100), index=True, nullable=True)
    magnitude = Column('magnitude', Float, index=True, nullable=True)
    longitude = Column('longitude', Float, index=True, nullable=True)
    latitude = Column('latitude', Float, index=True, nullable=True)
    depth = Column('depth', Float, index=True, nullable=True)
    eventtype = Column('type', String(100), index=True, nullable=True)
    seiscompid = Column('file', String(100), index=True, nullable=True)
    validated = Column('valid', Integer, index=True, nullable=True)
    projection = Column('projection', String(100), index=True, nullable=True)
    operator = Column('operator', String(100), index=True, nullable=True)
    last_modified = Column('timestamp', DateTime, index=True, nullable=True)
    last_modified_microsecond = Column(
        'timestamp_microsecond', Integer, index=True, nullable=True)
    count_deles = Column('deles', Integer, index=True, nullable=True)
    count_labuhan = Column('labuhan', Integer, index=True, nullable=True)
    count_pasarbubar = Column('pasarbubar', Integer, index=True, nullable=True)
    count_pusunglondon = Column(
        'pusunglondon', Integer, index=True, nullable=True)
    ml_deles = Column('ml_deles', Float, index=True, nullable=True)
    ml_labuhan = Column('ml_labuhan', Float, index=True, nullable=True)
    ml_pasarbubar = Column('ml_pasarbubar', Float, index=True, nullable=True)
    ml_pusunglondon = Column('ml_pusunglondon', Float,
                             index=True, nullable=True)
    location_mode = Column('locmode', String(255), index=True, nullable=True)
    location_type = Column('loctype', String(255), index=True, nullable=True)
    btbb = Column('btbb', JSON, nullable=True)
    cluster = Column('cluster', Integer, index=True, nullable=True)
    corr_coef = Column('corr_coef', Float, index=True, nullable=True)
