from crabmysql import CrabMysql

class Teacher(CrabMysql):
    name = CrabMysql.charField(max_length=20)


fields = ['teacher_id', 'name']
get_item = Teacher.get_object(fields)
print(get_item)
