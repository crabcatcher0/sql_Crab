# Custom ORM For SQLite

Basic Custom Object-Relational Mapping (ORM) system for SQLite, implemented in Python.


### Features:
- **Flask Integration:** Integration with Flask, providing web routing, request handling, and response rendering.

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