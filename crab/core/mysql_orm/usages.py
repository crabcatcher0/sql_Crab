from crabmysql import CrabMysql

class Teacher(CrabMysql):
    name = CrabMysql.charField(max_length=20)

get_item = Teacher.get_object_all()
print(get_item)
