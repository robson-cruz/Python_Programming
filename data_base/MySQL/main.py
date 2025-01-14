from sqlalchemy import create_engine, inspect, text
import os

MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

# Create a connection engine
engine = create_engine(f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306")

# Create an inspector object
inspector = inspect(engine)

# Get all databases from MySQL
db_names = inspector.get_schema_names()
print(db_names)

# Get all tables in "sakila" database
tables = inspector.get_table_names('sakila')
print(tables)

# Query data from the 'actor' table in the 'sakila' database
print()
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM sakila.actor LIMIT 10"))

    # print column names
    print(result.keys())

    # print rows
    for row in result:
        print(row)
