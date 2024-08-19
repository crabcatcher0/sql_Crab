# Custom ORM For SQLite

Basic Custom Object-Relational Mapping (ORM) system for SQLite, implemented in Python.


### Features:
- **Flask Integration:** Integration with Flask, providing web routing, request handling, and response rendering.

- **ORM:**
- Creates table with Auto Incremented Primary Key
- Table names are mapped to classes
- Define columns with data types like `varchar`, `integer`, `boolean`, `emailfield`.
- Converts database query results into `serialized` formats.
- `serializer` has methods like `all_data` and `one_data`.