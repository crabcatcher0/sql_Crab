# from add_data import Data
from .get_data import GetData
"""  Example to add Data  """


class Student(GetData):
    _data = {
        'name':'ram',
        'email': 'ram@gmail.com',
        'age': 12
    }


