from core.crabmodel import CrabModel
"""  Example to add Data  
"""


class Student(CrabModel):
    """
        : Table name wille set automatically as class name in lowercase
        : _data is a dict and keys are columns and values are data relative to that columns
    """
    
    _data = {
        'name':'ram',
        'email': 'ram@gmail.com',
        'age': 12
    }


class Teacher(CrabModel):
    _data = {
        'name':'kamal',
        'subject': 'math',
        'email': 'kamal@gmail.com',
        'is_substitute': True,

    }
    _data = {
        'name':'gita',
        'subject': 'science',
        'email': 'gita@gmail.com',
        'is_substitute': False,

    }


