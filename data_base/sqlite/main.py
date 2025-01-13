from sqlalchemy import create_engine, inspect, MetaData, Table

# Create a connection engine (adjust the path to your DB)
# https://stepik.org/media/attachments/lesson/511144/Buildings_Database.sqlite
engine = create_engine("sqlite:///Buildings_Database.sqlite", echo=False)

# Create an inspector object
inspector = inspect(engine)

# Get all database tables
table_names = inspector.get_table_names()

# Get the number of tables
num_tables = len(table_names)

# Print the table names and number of tables
print(table_names)
print(f"Number of tables: {num_tables}")

# get metadata from a table
metadata = MetaData()

# Reflect the table 'Buildings'
buildings_table = Table('Buildings', metadata, autoload_with=engine)

# Print the reflected table's representation
print()
print(repr(buildings_table))

print()
number_of_columns = 0
for column in buildings_table.columns:
    print(f"{column.name}: {column.type}")
    number_of_columns += 1

print("---------------------")
print(f"Number of columns: {number_of_columns}")

# Dispose the engine (optional)
engine.dispose()
