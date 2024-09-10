
from core.sqlite3_orm.crabmodel import CrabModel
from core.sqlite3_orm.datatypes import DataTypes

"""
    Create the class name as of table name,
    _column dict, where keys are column name and values are datatypes.
    
"""

class Student(CrabModel):
    _column = {
        'name': DataTypes.varchar(20),
        'email': DataTypes.emailfield(),
        'address': DataTypes.varchar(),
        'created_at': DataTypes.datetimefield()
    }





