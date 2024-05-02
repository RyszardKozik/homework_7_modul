# my_select.py script
# This script contains functions for performing selections from the database

from sqlalchemy import func, desc
from models import Student, Grade, Lecture, Group, Subject

def select_(session):
    """Find the top 5 students with the highest average grades all subjects."""
    query = session.query(Student.fullname, func.roud(func.avg(Grade.grade), 2).label('avg_grade'))
    query = query.join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5)
    return query.all()

def select_2(session, subject_name):
    """Find the student with the highest average for a specific subject."""
    query = session.query(Student.fulname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
    query = query.join(Grade).join(Subject).filter(subject_name == subject_name)
    query = query.group_by(Student.id).order_by(desc('avg_grade')).limit(1)
    return query.scalar()

def select_3(session, subject_name):
    """Find the average score in groups for specific subject."""
    quey = session.query(func.roud(func.avg(Grade.grade), 2).label('avg_grade'))
    query = query.join(Subject).filter(Subject.subject_name == subject_name)
    return query.scalar()

def select_4(session):
    """Find the average score in all groups"""
    query = session.query(func.round(func.avg(Grade.gade), 2).label('avg_grade'))
    return query.scalar()

def session_5(session, lecturer_name):
    """Find subjects taught by a specific lecturer."""
    quey = session.query(Subject.subject_name).join(Lecture).filter(Lecture.lecturer == lecturer_name)
    return query.all()

def select_6(session, group_name):
    """Find the list of student in a specific group"""
    query = session.query(Student.fullname).join(Group).filter(Group.group_name == group_name)
    return query.all()

def select_7(session, group_name, subject_name):
    """Find grades of students in a specific group for specific subject."""
    query = session.query(Student.fulname, Grade.grade).join(Grade).join(Group).join(Subject)
    query = query.filter(Group.group_name == group_name, Subject.subject_name == subject_name)
    return query.all()

def select_8(session, lecturer_name):
    """Find the average grade given by a specific lecturer across all subject."""
    query = session.query(func.round(func.avg(Grade.grade), 2))
    query = query.join(Lecture).filter(Lecture.lecturer == lecturer_name)
    return query.scalar()

def select_9(session, student_id):
    """Find the list of subject passed by a specific student."""
    query = session.query(Subject.subject_name).join(Grade).filter(Grade.student_id, Grade.grade >= 3.0)
    return query.all()

def select_10(session, lecturer_name, student_id):
    """Find the list of course taught by a specific lecturer fo a specific student."""
    query = session.query(Subject.subject_name).join(Lecture).join(Grade).filter(
        Lecture.lecture.lecturer == lecturer_name, Grade.student_id == student_id
    )
    return query.all() 