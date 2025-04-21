import psycopg2
import csv
from config import load_config

#path: /Users/adilet/Desktop/PPHM/labs/lab10/example.csv

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def create_table(conn):
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone VARCHAR(20),
        email VARCHAR(100)
    );
    """
    try:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    except Exception as e:
        print("Error creating table:", e)
        conn.rollback()

def insert_from_csv(conn, csv_path):
    try:
        with open(csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) 
            with conn.cursor() as cur:
                for row in reader:
                    try:
                        cur.execute(
                            "INSERT INTO phonebook (username, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING;",
                            (row['username'], row['first_name'], row['last_name'], row['phone'], row['email'])
                        )
                    except Exception as e:
                        print(f"Error inserting row {row}: {e}")
                conn.commit()
                print("Data inserted successfully.")
    except Exception as e:
        print("Error CSV file:", e)

def insert_console(conn):
    username = input("Enter username: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook (username, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING;",
                (username, first_name, last_name, phone, email)
            )
            conn.commit()
            print("Record inserted successfully.")
    except Exception as e:
        print("Error inserting record:", e)
        conn.rollback()

def update(conn):
    username = input("Enter the username to update: ").strip()
    print("Which field would you like to update? \n1. Phone\n2. Email")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        new_value = input("Enter new phone: ").strip()
        field = "phone"
    elif choice == "2":
        new_value = input("Enter new email: ").strip()
        field = "email"
    else:
        print("Invalid selection.")
        return

    try:
        with conn.cursor() as cur:
            cur.execute(
                f"UPDATE phonebook SET {field} = %s WHERE username = %s;",
                (new_value, username)
            )
            if cur.rowcount == 0:
                print("No record found with that username.")
            else:
                conn.commit()
                print("Updated successfully.")
    except Exception as e:
        print("Error updating...", e)
        conn.rollback()

def query(conn):
    print("Query options: \n1. All records\n2. Filter by username\n3. Filter by phone\n4. Filter by email")
    choice = input("Enter your choice (1/2/3/4): ").strip()
    sql = ""
    value = None

    if choice == "1":
        sql = "SELECT id, username, first_name, last_name, phone, email FROM phonebook;"
    elif choice == "2":
        username = input("Enter the username to search: ").strip()
        sql = "SELECT id, username, first_name, last_name, phone, email FROM phonebook WHERE username ILIKE %s;"
        value = f"%{username}%"
    elif choice == "3":
        phone = input("Enter the phone to search: ").strip()
        sql = "SELECT id, username, first_name, last_name, phone, email FROM phonebook WHERE phone ILIKE %s;"
        value = f"%{phone}%"
    elif choice == "4":
        email = input("Enter the email to search: ").strip()
        sql = "SELECT id, username, first_name, last_name, phone, email FROM phonebook WHERE email ILIKE %s;"
        value = f"%{email}%"
    else:
        print("Invalid option.")
        return

    try:
        with conn.cursor() as cur:
            if value is None:
                cur.execute(sql)
            else:
                cur.execute(sql, (value,))
            records = cur.fetchall()
            if records:
                print("Results:")
                for record in records:
                    print(f"ID: {record[0]}, Username: {record[1]}, First Name: {record[2]}, Last Name: {record[3]}, Phone: {record[4]}, Email: {record[5]}")
            else:
                print("No records found.")
    except Exception as e:
        print("Error querying records:", e)

def delete(conn):
    username = input("Enter the username of the record to delete: ").strip()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE username = %s;", (username,))
            if cur.rowcount == 0:
                print("No record found with that username.")
            else:
                conn.commit()
                print("Record deleted successfully.")
    except Exception as e:
        print("Error deleting record:", e)
        conn.rollback()

def clear_db(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS phonebook;")
            conn.commit()
            print("Database cleared successfully.")
    except Exception as e:
        print("Error clearing database:", e)
        conn.rollback()


def main():
    config = load_config()
    conn = connect(config)
    create_table(conn)

    while True:
        print("\n----- PHONEBOOK MENU -----")
        print("1. Insert data from CSV")
        print("2. Insert data in console")
        print("3. Update")
        print("4. Query")
        print("5. Delete by username")
        print("6. Clear database")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            csv_path = input("Enter path to CSV file: ").strip()
            insert_from_csv(conn, csv_path)
        elif choice == "2":
            insert_console(conn)
        elif choice == "3":
            update(conn)
        elif choice == "4":
            query(conn)
        elif choice == "5":
            delete(conn)
        elif choice == "6":
            clear_db(conn)
            create_table(conn)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("ERROR. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
