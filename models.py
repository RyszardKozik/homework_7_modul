from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Table for the many-to-many relationship between the 'notes' and 'tags' tables
note_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("note_id", Integer, ForeignKey("notes.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
)

# 'Notes' table, where task names will be stored
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.now())
    records = relationship("Record", cascade="all, delete", backref="note")
    tags = relationship("Tag", secondary=note_m2m_tag, backref="notes", passive_deletes=True)

# 'Records' table, where records of tasks for a specific note from the 'notes' table will be stored - one-to-many relationship, 'note_id' field
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)
    note_id = Column(Integer, ForeignKey(Note.id, ondelete="CASCADE"))

# 'Tags' table, which stores a set of tags for a to-do list
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="students")

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", back_populates="group")

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Lecturer(Base):
    __tablename__ = 'lecturers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'))
    grade = Column(Float)
    date = Column(Date)

    student = relationship("Student", backref="grades")
    subject = relationship("Subject", backref="grades")
    lecturer = relationship("Lecturer", backref="grades")
