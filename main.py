#!/usr/bin/env python3
from sqlalchemy import Column, Index, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__='students'
    #table columns
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    index = Column(Integer())


if __name__=='__main__':
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    #reading data
    students = session.query(Student).all()
    print([student.name for student in students if student.id==1])
    #deleting data
    # studentD = session.query(Student).filter(Student.name.like("%Max%")).first()
    # studentD = session.query(Student).filter(Student.id == 4).first()
    # session.delete(studentD)
    # session.commit()
    #create data function with sqlalchemy
    # studentA = Student(name='Max',index=123)
    # studentB = Student(name='John Doe',index=456)
    # session.bulk_save_objects([studentA,studentB])
    # session.commit()
    #update data 
    session.query(Student).update({Student.name:"John Doe"})
    session.commit()

