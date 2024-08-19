from core.crabmodel import CrabModel
from core.add_data import Data
from core.datatypes import DataTypes


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


class Teacher(Data):
    _data = {
        'name': 'kamal',
        'email': 'kamal@gmail.com',
        'subject': 'science'
    }