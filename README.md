# Custom ORM For SQLite And MYSQL

Basic Custom Object-Relational Mapping (ORM) system for SQLite and MYSQL implemented in Python.


### Features:
- **Flask Integration:** Integration with Flask to document entire project.

- **ORM:**
- Creates table with Auto Incremented Primary Key
- Table names are mapped to classes
- Define columns with data types like `varchar`, `integer`, `boolean`, `emailfield`, `datetimefield`.
- Converts database query results into `serialized` formats.
- `serializer` has methods like `all_data` and `one_data`.
- Adding records are handled through `YourModel.add_data(column={dict}})`.
- Deleting records are handled through `YourModel.delete(pk={record's.id})`.
- `get_data`  retrieve a single record from the database based on the provided query parameters.
    ```python
    #Example
    user = User.get_data(email="youremail")
    if user:
        print(f"User found: {user.user_name} {user.user_age}")
    else:
        print("User not found.")

    ```
- **Foreign Key:**

- ```python

    class YourModel(CrabModel):
        _column = { # _column: A dictionary that defines the columns of the table or model.
            'col_1': DataTypes.integer(),
            'col_2': DataTypes.integer()
        }

        foreign_keys = [ #foreign_keys: A list that defines the foreign key constraints for table.

            ForeignKey.create_foreignkey(field_name='col_1', model='model_name'),
            ForeignKey.create_foreignkey(field_name='col_2', model='second_model')
        ]

    ```
- **`filter_data` Method**
- `filter_data` method is a class method to filter records from the database table associated with the class. It retrieves rows from the specified table where a given column matches a specified value and returns these rows as a list of dictionaries.

    ```python

    #Example:
    results = YourModel.filter_data('field_name', 'value')
    print(results)
    [{'id': 1, 'column_name': 'value', 'other_column': 'other_value'}, ...] #output
    ```

- **`order_by` Method**
The `order_by` method allows to fetch records from the database ordered by a specific column. This method is implemented as a class method, meaning it can be called directly on a model class.

- Returns records from a table and order them by a column name in `dict` form.
    ```python

    #Example
    result = YourModel.order_by('created_at', descending=True) #flag indicating whether to sort in descending order by default it is False.
    print(result)