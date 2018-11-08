# db_creator.py
 
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///staffinginfo.db', echo=True)
Base = declarative_base()
 
 
class Staffing(Base):
    __tablename__ = "staffing"
 
    id = Column(Integer, primary_key=True)
    work_period = Column(String)
    employee_name = Column(String)
    client_name = Column(String)
    role = Column(String)
    time_spent = Column(String)
	
	 
# create tables
Base.metadata.create_all(engine)