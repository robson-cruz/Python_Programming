import sqlite3

# Initialize the connection variable
conn = None

try:
    # Connects to the SQLite database file pet_db.db. If the file doesn't exist, it creates one.
    conn = sqlite3.connect("pet_database.db")

    # Create a Cursor object to execute SQL commands in the database
    cursor = conn.cursor()

    # Create a Table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        species TEXT,
        age INTEGER
        )"""
    )

    # Define multiple entries
    some_pets = [
        ("Lassie", "dog", 3),
        ("Chewbacca", "dog", 1),
        ("Fluff-Ball", "cat", 4),
        ("Captain", "parrot", 2)
    ]

    # Insert entries into the table, checking for duplicates
    for pet in some_pets:
        cursor.execute("INSERT OR IGNORE INTO pets (name, species, age) VALUES (?, ?, ?)", pet)

    # Commit the changes
    conn.commit()

    # Query the Database
    cursor.execute("SELECT rowid,* FROM pets WHERE species == 'dog'")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the Connection
    if conn:
        conn.close()
