import random
from faker import Faker
from main import Student
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

Base =  declarative_base()
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

fake=Faker()
students = [
    Student(
        name= fake.name(),
        index= random.randint(900,1900)
    )
    for i in range(20)]

session.bulk_save_objects(students)
session.commit()