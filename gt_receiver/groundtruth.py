from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Groundtruth(Base):
    __tablename__ = 'groundtruths'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    activity = Column(String)
    user = Column(Integer)
