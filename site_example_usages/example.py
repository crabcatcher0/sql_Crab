from crab_sql.crabmodel import CrabModel
from crab_sql.datatypes import DataTypes

class Teacher(CrabModel): # Teacher as table name
    _columns = {
        "name": DataTypes.varchar(max_length=24),
        "email": DataTypes.emailfield(unique=True)
    }



new_teacher = Teacher()
print(new_teacher)