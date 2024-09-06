from .get_data import GetData

"""

Database result it converted into list of dict   

"""

class Serializer:
    
    @staticmethod
    def all_data(model: str, fields: tuple):
        """
        Fetches all records for a given model and serializes them into a list of dictionaries.

        :param model: The name of the model to query.
        :param fields: A tuple of field names to include in the result.
        :return: A list of dictionaries, each representing a row of data.
        """
        try:
            data = GetData.get_data(model, fields=fields)
            tup_data = tuple(data)

            final_result = []
            for tup in tup_data:
                zip_data = dict(zip(fields, tup))
                final_result.append(zip_data)
                
        except Exception as e:
            print(f"Error on serializer: {str(e)}")

        return final_result
    
    
    @staticmethod
    def one_data(model: str, fields: tuple, pk: int):
        """
        Fetches a single record by primary key and serializes it into a dictionary.

        :param model: The name of the model to query.
        :param fields: A tuple of field names to include in the result.
        :param pk: The primary key of the record to fetch.
        :return: A dictionary representing the row of data.
        """
        data = GetData.get_one(model, fields, pk=pk)
        result = dict(zip(fields, data))
        return result
        





    
    
    











