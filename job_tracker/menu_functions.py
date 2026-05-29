from packages import sqlite3
from setup import setup_database

setup_database()

# add_application() function to commit changes to the db
def add_application():
        # Ask for inputs from the user
        company = input("Enter company name: ")
        role = input("Enter the position/role: ")
        date_applied = input("Date applied (YYYY-MM-DD): ")
        status = input("Status of the application (Applied, Interviewing, Rejected, Offered): ")
        notes = input("Add any extra notes (optional): ")

        # Connect to the database and get the cursor
        db = sqlite3.connect("jobs.db")
        cur = db.cursor()

        # INSERT data into the 'application table
        cur.execute("""
            INSERT INTO applications (company, 
                                        role,
                                        date_applied,
                                        status,
                                        notes) 
            VALUES (?, ?, ?, ?, ?);
            """, (company, role, date_applied, status, notes))

        # Commit the changes and close the connection 
        db.commit()
        db.close()
        print("Entry added successfully!")


# view_appplication() function to view the existing entries
def view_application():
        # Connect to the database and the cursor 
        db = sqlite3.connect("jobs.db")
        cur = db.cursor()

        # Add SELECT statement to a variable 
        cur.execute(""" SELECT 
                        id,
                        company,
                        role,
                        status
                        FROM applications """)

        # Fetch the data from the table
        rows = cur.fetchall() # fetchall() returns list of rows as tuples

        # Print the entries using a loop
        print("\n--- CURRENT JOB PIPELINE ---")
        for row in rows:
#                print(row)
                print(f"ID: {row[0]} | Company: {row[1]} | Role: {row[2]}, Status: {row[3]}")
        
        db.close


# update_status() function to update/alter the table
def update_status():
        # Get inputs from the users
        new_status = input("What is the current status of the application? ")
        id = input("What is the ID of the application that you want to update? ")

        # Connect to the database and the cursor 
        db = sqlite3.connect("jobs.db")
        cur = db.cursor()

        # Update the table
        cur.execute(""" UPDATE applications
                        SET status = ?
                        WHERE id = ?
                    """, (new_status, id))
        db.commit()
        db.close()
        print("Status updated successfully!")



# delete_application() function to remove records from the table
def delete_application():
        # Get inputs from the users
        id = input("What is the ID of the application you would like to delete? ")
        confirm = input("Are you sure you want to complete this action? (y/n): ")

        # Actions based on the user's inputs
        if confirm.lower() == 'y':
                # Connect to the database and the cursor 
                db = sqlite3.connect("jobs.db")
                cur = db.cursor()
                # Update the table
                cur.execute(""" DELETE FROM applications
                    WHERE id = ?""", (id,))
                db.commit()
                db.close()
                print("Application #{id} has been deleted.")
        else:
                print("Deletion cancelled.")



# view_dashboard() function for an overview of the job search
def view_dashboard():
        # Connect to the database and the cursor 
        db = sqlite3.connect("jobs.db")
        cur = db.cursor()

        # Count the total number of applications in the database
        cur.execute(""" SELECT COUNT(*)
                                  FROM applications; """)
        count_total = cur.fetchone()[0]
        
        # Count the total number of applications with specific status
        cur.execute(""" SELECT COUNT(*) 
                                      FROM applications
                                      WHERE status = 'Interviewing'; """)
        count_interview = cur.fetchone()[0]
        
        # Print the results 
        print(f"The total number of the application: {count_total}")
        print(f"The number of application currently set to status 'Interviewing': {count_interview}")

        db.close()