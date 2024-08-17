from datatypes import DataTypes
from crabmodel import CrabModel


class Student(CrabModel):
    _column = {
        'name': DataTypes.varchar(20),
        'email': DataTypes.varchar(),
        'age': DataTypes.integer(),
    }
    role = CrabModel.add_column('student', 'role', DataTypes.boolean())
