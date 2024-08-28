from core.crabmodel import CrabModel
from usage import Student, Course, Enrollment
"""  Example to add Data  
"""


def data_std():
    data = {
        'name': 'ram',
        'email': 'ram@gmail.com',
        'address': 'Kathmandu'
    }
    context = Student.add_data(data)
    return context


def data_course():
    data = {
        'course_name': 'Computer Science',
        'course_code': 'CS101'
    }
    context = Course.add_data(data)
    return context


def data_enroll():
    data = {
        'student_id': 1,
        'enrolled_course': 1
    }
    context = Enrollment.add_data(data)
    return context


data_std()
data_course()
data_enroll()