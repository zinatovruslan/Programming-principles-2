import psycopg2
import csv
from tabulate import tabulate

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "12345678",  
    "port": "5432"
}

# Connect to the database
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Create phonebook table
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL UNIQUE
)
""")
conn.commit()

# Function to insert data from console
def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.callproc("insert_or_update_user", (name, surname, phone))
    conn.commit()
    print("Data successfully added or updated!")

# Function to insert data from CSV
def insert_from_csv(filepath):
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            users_list = []
            for row in reader:
                users_list.append(row)
        cur.callproc("insert_multiple_users", (users_list,))
        invalid_data = cur.fetchone()[0]
        if invalid_data:
            print("Invalid data found:", invalid_data)
        else:
            print("Data from CSV successfully added!")
        conn.commit()
    except FileNotFoundError:
        print("File not found. Check the path.")

# Function to search data by pattern
def search_data():
    pattern = input("Enter search pattern (part of name, surname, or phone): ")
    cur.callproc("search_phonebook", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Function to query data with pagination
def query_paginated_data():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.callproc("get_paginated_phonebook", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Function to delete data
def delete_data():
    choice = input("Delete by (name/phone): ").strip().lower()
    if choice == "name":
        name = input("Enter name to delete: ")
        cur.callproc("delete_phonebook_entry", (name, None))
    elif choice == "phone":
        phone = input("Enter phone to delete: ")
        cur.callproc("delete_phonebook_entry", (None, phone))
    else:
        print("Invalid choice.")
        return
    conn.commit()
    print("Data successfully deleted!")

# Function to display all data
def display_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Main program loop
while True:
    print("""
    Commands:
    1. Insert data (console/csv)
    2. Search data by pattern
    3. Query data with pagination
    4. Delete data
    5. Display all data
    6. Exit
    """)
    command = input("Enter command: ").strip().lower()

    if command == "1":
        method = input("Choose method (console/csv): ").strip().lower()
        if method == "console":
            insert_from_console()
        elif method == "csv":
            filepath = input("Enter path to CSV file: ")
            insert_from_csv(filepath)
        else:
            print("Invalid method. Choose console or csv.")
    elif command == "2":
        search_data()
    elif command == "3":
        query_paginated_data()
    elif command == "4":
        delete_data()
    elif command == "5":
        display_all()
    elif command == "6":
        print("Program terminated.")
        break
    else:
        print("Invalid command. Try again.")

# Close connection
cur.close()
conn.close()
