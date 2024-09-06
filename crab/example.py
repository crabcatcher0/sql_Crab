from core.crabmodel import CrabModel
from usage import Student, Course, Enrollment
    


"""  Example to add Data  
"""


def data_std():
    data = {
        'name': 'gita',
        'email': 'gita@gmail.com',
        'address': 'Lokanthali'
    }
    context = Student.add_data(data)
    return context


data_std()


# def edit():
#     columns=['name', 'email'],
#     values=['shyam', 'shyam@gmail.com'],
#     pk=1
#     data = Student.update(columns=columns, values=values, pk=pk)
    
#     return data

# edit()

data = Student.order_by('created_at', descending=True)
print(data)