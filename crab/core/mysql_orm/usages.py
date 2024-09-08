from main import CrabMysql


class Student(CrabMysql):
    name = CrabMysql.charField(max_length=12)
    age = CrabMysql.intField()
    gender = CrabMysql.charField(max_length=23)
    name = CrabMysql.new_field('student', 'name', CrabMysql.charField())
