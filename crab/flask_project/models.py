from crab.core.crabmodel import CrabModel
from crab.core.datatypes import DataTypes


class Student(CrabModel):
    _column = {
        'name': DataTypes.varchar(max_length=20),
        'email': DataTypes.emailfield(unique=True),
        'age': DataTypes.integer()
    }
    



class Teacher(CrabModel):
    _column = {
        'name': DataTypes.varchar(max_length=20),
        'email': DataTypes.emailfield(unique=True),
        'subject': DataTypes.varchar(max_length=30)
    }


