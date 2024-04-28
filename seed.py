# seed.py script
# This script populates the database with random data using Faker

import os
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import Student, Group, Subject, Lecturer, Grade
import random

# Load environment variables from .env file
load_dotenv()

# Create Faker instance
fake = Faker()

# Connect to the database
DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/postgres'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define functions to generate random data
def create_students(num_students):
    for _ in range(num_students):
        student = Student(name=fake.name())
        session.add(student)

def create_groups(num_groups):
    for i in range(num_groups):
        group = Group(name=f"Group {i+1}")
        session.add(group)

def create_subjects(num_subjects):
    for i in range(num_subjects):
        subject = Subject(name=f"Subject {i+1}")
        session.add(subject)

# Add more functions to create random data for lecturers, grades, etc.

# Call the functions to generate random data
create_students(30)
create_groups(3)
create_subjects(8)

# Commit the changes
session.commit()