from crab import Crab
from datatypes import DataTypes


class Teacher(Crab):
    columns = {
        'name': DataTypes.varchar(),
        'age': DataTypes.integer(),
        'email': DataTypes.varchar(),
        'classes': DataTypes.varchar()
    }


