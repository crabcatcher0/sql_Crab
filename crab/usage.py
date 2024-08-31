from core.datatypes import DataTypes
from core.crabmodel import CrabModel, ForeignKey
from core.get_data import GetData
"""
    Create the class name as of table name,
    _column dict, where keys are column name and values are datatypes.
    
"""

class Student(CrabModel):
    _column = {
        'name': DataTypes.varchar(20),
        'email': DataTypes.emailfield(),
        'address': DataTypes.varchar(),
    }


class Course(CrabModel):
    _column = {
        'course_name': DataTypes.varchar(max_length=20, unique=True),
        'course_code': DataTypes.varchar(max_length=20, unique=True)
    }


class Enrollment(CrabModel):
    _column = {
        'student_id': DataTypes.integer(),
        'enrolled_course': DataTypes.integer()
    }

    foreign_keys = [
    ForeignKey.create_foreignkey('student_id', 'student'),
    ForeignKey.create_foreignkey('enrolled_course', 'course')
    ]



