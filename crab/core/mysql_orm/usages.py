from crabmysql import CrabMysql

class Teacher(CrabMysql):
    name = CrabMysql.charField(max_length=20)
    email = CrabMysql.add_field('teacher', 'email', CrabMysql.charField())