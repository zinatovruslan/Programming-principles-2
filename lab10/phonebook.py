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
    phone VARCHAR(255) NOT NULL
)
""")
conn.commit()

# Function to insert data from console
def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    conn.commit()
    print("Data successfully added!")

# Function to insert data from CSV
def insert_from_csv(filepath):
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
        conn.commit()
        print("Data from CSV successfully added!")
    except FileNotFoundError:
        print("File not found. Check the path.")

# Function to update data
def update_data():
    column = input("Enter column to update (name, surname, phone): ")
    old_value = input(f"Enter current value in column {column}: ")
    new_value = input(f"Enter new value for column {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, old_value))
    conn.commit()
    print("Data successfully updated!")

# Function to query data
def query_data():
    column = input("Enter column to filter by (id, name, surname, phone): ")
    value = input(f"Enter value for column {column}: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="fancy_grid"))

# Function to delete data
def delete_data():
    phone = input("Enter phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
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
    2. Update data
    3. Query data
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
        update_data()
    elif command == "3":
        query_data()
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
