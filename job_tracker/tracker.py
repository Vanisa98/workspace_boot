# Import from necessary packages, functions
from packages import sqlite3
from setup import setup_database
from menu_functions import add_application, view_application, update_status, delete_application, view_dashboard


# Loop for data validation and main menu
setup_database()

while True:
    print("\n=== JOB APPLICATION TRACKER ===")
    print("1. View Current Application List")
    print("2. Add New Application")
    print("3. Update Application Status")
    print("4. Exit")
    print("5. Delete Application")
    print("6. View the dashboard")
    
    # Grab menu choice
    choice = input("Which option do you want to choose? (Please type the number) ")

    # Routing the choices to respective functions
    if choice == "4":
           print("Goodbye!")
           break
    
    elif choice == "1":
           view_application()

    elif choice == "2":
           add_application()

    elif choice == "3":
           update_status()
       
    elif choice == "5":
           delete_application()

    elif choice == '6':
           view_dashboard()
           
    else:
           print("\n[Error] Invalid choice. Please enter a number from 1 to 6")










# --------------------------------------------------------
# Make sure the database and the table exists
# setup_database()

# Add entry to the database and table
# add_application()


# View the table entries
# view_application()

# Update the database and table
# update_status()
