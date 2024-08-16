from crab import Crab, DataTypes


class Student(Crab):
    _columns = {
        'name': DataTypes.varchar(),
        'age' : DataTypes.integer()
    }