# Import from packages.py
from packages import sqlite3


# The function to set up the database and add a new table
def setup_database():
    # Connect to jobs.db
    db = sqlite3.connect("jobs.db")

    # Call the database cursor in order to execute SQL statements 
    cur = db.cursor()

    # Create table 'applications' inside jobs.db 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT,
            status TEXT,
            notes TEXT
            )""")

    # Verify that the table has been created
    cur.execute(""" SELECT name FROM sqlite_master; """)
    table_exists = cur.fetchone()

    # Commit changes to the file 
    db.commit()
    print("Database and table initialized successfully!")

    # Close the connection
    db.close()


setup_database()