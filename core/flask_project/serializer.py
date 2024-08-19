from core.serializer import Serializer



def viewserial():
    model = 'student'
    fields = ('id', 'name', 'email', 'age')
    data = Serializer.all(model=model, fields=fields)
    return data