from crabmodel import CrabModel
from datatypes import DataTypes


class Teacher(CrabModel):  # teacher as table name
    _columns = {
        "name": DataTypes.varchar(max_length=24),
        "email": DataTypes.emailfield(unique=True),
    }


new = Teacher.add_data({"name": "John", "email": "John@gmail.com"})
