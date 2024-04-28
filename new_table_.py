from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker
import random

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Faker instance for generating random data
fake = Faker()

# Create a PostgreSQL database engine
DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/postgres'
engine = create_engine(DATABASE_URL)

# Create a base instance for SQLAlchemy models
Base = declarative_base()

# Define SQLAlchemy models for tables
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', backref='group')

class Lecturer(Base):
    __tablename__ = 'lecturers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject', backref='lecturer')

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'))

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(String)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to fill tables with random data
def fill_tables():
    # Fill the students table
    for _ in range(30):
        student = Student(name=fake.name())
        session.add(student)

    # Fill the groups table
    for _ in range(3):
        group = Group(name=f'Group {_}')
        session.add(group)

    # Fill the lecturers table
    for _ in range(3):
        lecturer = Lecturer(name=fake.name())
        session.add(lecturer)

    # Fill the subjects table
    for _ in range(5, 9):
        for _ in range(3):
            subject = Subject(name=fake.word(), lecturer_id=random.randint(1, 3))
            session.add(subject)

    # Fill the grades table
    for student_id in range(1, 31):
        for _ in range(random.randint(5, 9)):
            grade = Grade(student_id=student_id, subject_id=random.randint(1, 3), grade=random.randint(2, 5), date=fake.date())
            session.add(grade)

    # Commit changes to the session
    session.commit()

# Functions to execute queries
def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label('avg_grade')).join(Grade, Student.id == Grade.student_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()

# Call the function to fill tables with data
fill_tables()

# Call the select_1 function and display the results
print("5 students with the highest average grades across all subjects:")
results = select_1()
for result in results:
    print(result)

# Close the session
session.close()