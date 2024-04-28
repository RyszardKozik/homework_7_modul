# my_select.py script
# This script contains functions for performing selections from the database

from sqlalchemy import func, desc
from models import Student, Grade

def select_top_students(session, num_students):
    """Find the top N students with the highest average grades across all subjects."""
    query = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))
    query = query.join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(num_students)
    return query.all()

# Add more functions for other queries

# Example usage:
# result = select_top_students(session, 5)
# print(result)