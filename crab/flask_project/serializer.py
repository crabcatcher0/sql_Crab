from crab.serializer import Serializer

def serializer(model: str, fields: tuple):
    data = Serializer.all_data(model=model, fields=fields)
    return data
