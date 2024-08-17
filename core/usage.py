from datatypes import DataTypes
from crabmodel import CrabModel


"""
    Create the class name as of table name,
    _column dict, where keys are column name and values are datatypes.

"""

class Student(CrabModel):
    _column = {
        'name': DataTypes.varchar(20),
        'email': DataTypes.varchar(),
        'age': DataTypes.integer(),
    }
    role = CrabModel.add_column(   ### add 'role' as new column to student table
        table_name = 'student', 
        column_name = 'role', 
        data_type = DataTypes.boolean()
    )


class Teacher(CrabModel):
    _column = {
        'name': DataTypes.varchar(max_length=20),
        'subject': DataTypes.varchar(max_length=30),
        'email' : DataTypes.varchar(),
        'is_substitute': DataTypes.boolean()
    }