from datatypes import DataTypes
from crabmodel import CrabModel
from add_data import Data
from get_data import GetData
"""
    Create the class name as of table name,
    _column dict, where keys are column name and values are datatypes.
    
"""

# class Student(CrabModel):
#     _column = {
#         'name': DataTypes.varchar(20),
#         'email': DataTypes.emailfield(),
#         'age': DataTypes.integer(),
#     }



#     role = CrabModel.add_column(   ### add 'role' as new column to student table
#         table_name = 'student', 
#         column_name = 'role', 
#         data_type = DataTypes.boolean()
#     )


# class Teacher(CrabModel):
#     _column = {
#         'name': DataTypes.varchar(max_length=20),
#         'subject': DataTypes.varchar(max_length=30),
#         'email' : DataTypes.varchar(),
#         'is_substitute': DataTypes.boolean()
#     }



# def show():
#     data = GetData.get_data('student')
#     result = [list(tpl) for tpl in data]
#     return result

# print(show())