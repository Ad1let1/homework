import psycopg2
import csv
from config import load_config

def connect(config):
    conn = psycopg2.connect(**config)
    print('Connected')
    return conn

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
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()

def insert_from_csv(conn, csv_path):
    csvfile = open(csv_path, mode='r', newline='', encoding='utf-8')
    reader = csv.DictReader(csvfile)
    cur = conn.cursor()
    for row in reader:
        cur.execute("INSERT INTO phonebook (username, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING;", 
                    (row['username'], row['first_name'], row['last_name'], row['phone'], row['email']))
    conn.commit()
    cur.close()
    csvfile.close()
    print("Data inserted successfully")

def insert_console(conn):
    username = input("Enter username: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (username, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING;", 
                (username, first_name, last_name, phone, email))
    conn.commit()
    cur.close()
    print("Record inserted successfully")

def update(conn):
    username = input("Enter the username to update: ").strip()
    print("Which field would you like to update?\n1. Phone\n2. Email")
    choice = input("Enter choice (1/2): ").strip()
    if choice == "1":
        new_value = input("Enter new phone: ").strip()
        field = "phone"
    elif choice == "2":
        new_value = input("Enter new email: ").strip()
        field = "email"
    else:
        print("Invalid selection")
        return
    cur = conn.cursor()
    cur.execute(f"UPDATE phonebook SET {field} = %s WHERE username = %s;", (new_value, username))
    conn.commit()
    cur.close()
    print("Updated successfully")

def query(conn):
    print("Query options:\n1. All records\n2. Filter by username\n3. Filter by phone\n4. Filter by email")
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
        print("Invalid option")
        return
    cur = conn.cursor()
    if value is None:
        cur.execute(sql)
    else:
        cur.execute(sql, (value,))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Username: {record[1]}, First Name: {record[2]}, Last Name: {record[3]}, Phone: {record[4]}, Email: {record[5]}")
    else:
        print("No records found")

def delete(conn):
    username = input("Enter the username of the record to delete: ").strip()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE username = %s;", (username,))
    conn.commit()
    cur.close()
    print("Record deleted successfully")

def clear_db(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS phonebook;")
    conn.commit()
    cur.close()
    print("Database cleared successfully")

def search_by_pattern(conn):
    pattern = input("Enter search pattern: ").strip()
    search_pattern = f"%{pattern}%"
    sql = "SELECT id, username, first_name, last_name, phone, email FROM phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone ILIKE %s;"
    cur = conn.cursor()
    cur.execute(sql, (search_pattern, search_pattern, search_pattern))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Username: {record[1]}, First Name: {record[2]}, Last Name: {record[3]}, Phone: {record[4]}, Email: {record[5]}")
    else:
        print("No records found")

def upsert_by_name_phone(conn):
    username = input("Enter username: ").strip()
    phone = input("Enter phone: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;", 
                (username, phone))
    conn.commit()
    cur.close()
    print("User upserted successfully")

def batch_upsert_users(conn):
    usernames = []
    phones = []
    while True:
        username = input("Имя: ").strip()
        if not username:
            break
        phone = input("Телефон: ").strip()
        usernames.append(username)
        phones.append(phone)
    cur = conn.cursor()
    cur.execute("SELECT * FROM upsert_many_users(%s, %s);", (usernames, phones))
    incorrect = cur.fetchall()
    conn.commit()
    cur.close()
    if incorrect:
        for row in incorrect:
            print(f"Username: {row[0]}, Phone: {row[1]}")
    else:
        print("Все пользователи обработаны корректно")

def query_with_pagination(conn):
    limit = int(input("Введите лимит: ").strip())
    offset = int(input("Введите смещение (offset): ").strip())
    cur = conn.cursor()
    cur.execute("SELECT id, username, first_name, last_name, phone, email FROM phonebook LIMIT %s OFFSET %s;", (limit, offset))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Username: {record[1]}, First Name: {record[2]}, Last Name: {record[3]}, Phone: {record[4]}, Email: {record[5]}")
    else:
        print("Записи не найдены для данной страницы")

def delete_by_username_or_phone(conn):
    choice = input("Удалить по:\n1. Username\n2. Phone\nВведите выбор (1/2): ").strip()
    if choice == "1":
        value = input("Введите username: ").strip()
        field = "username"
    elif choice == "2":
        value = input("Введите phone: ").strip()
        field = "phone"
    else:
        print("Неверный выбор")
        return
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s;", (value,))
    conn.commit()
    cur.close()
    print("Запись удалена успешно")

def upsert(conn):
    username = input("Enter username: ").strip()
    phone = input("Enter phone: ").strip()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;", (username, phone))
    conn.commit()
    cur.close()
    print("User upserted successfully")

def batch_upsert(conn):
    usernames = []
    phones = []
    while True:
        username = input("Имя: ").strip()
        if not username:
            break
        phone = input("Телефон: ").strip()
        usernames.append(username)
        phones.append(phone)
    cur = conn.cursor()
    cur.execute("SELECT * FROM upsert_many_users(%s, %s);", (usernames, phones))
    incorrect = cur.fetchall()
    conn.commit()
    cur.close()
    if incorrect:
        for row in incorrect:
            print(f"Username: {row[0]}, Phone: {row[1]}")
    else:
        print("Все пользователи обработаны корректно")

def paginated_query(conn):
    limit = int(input("Введите лимит: ").strip())
    offset = int(input("Введите смещение (offset): ").strip())
    cur = conn.cursor()
    cur.execute("SELECT id, username, first_name, last_name, phone, email FROM phonebook LIMIT %s OFFSET %s;", (limit, offset))
    records = cur.fetchall()
    cur.close()
    if records:
        for record in records:
            print(f"ID: {record[0]}, Username: {record[1]}, First Name: {record[2]}, Last Name: {record[3]}, Phone: {record[4]}, Email: {record[5]}")
    else:
        print("Записи не найдены для данной страницы")

def delete_by_field(conn):
    choice = input("Удалить по:\n1. Username\n2. Phone\nВведите выбор (1/2): ").strip()
    if choice == "1":
        value = input("Введите username: ").strip()
        field = "username"
    elif choice == "2":
        value = input("Введите phone: ").strip()
        field = "phone"
    else:
        print("Неверный выбор")
        return
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s;", (value,))
    conn.commit()
    cur.close()
    print("Запись удалена успешно")

def main():
    config = load_config()
    conn = connect(config)
    create_table(conn)
    while True:
        print("\n1. Insert data from CSV")
        print("2. Insert data in console")
        print("3. Update")
        print("4. Query")
        print("5. Delete by username")
        print("6. Clear database")
        print("7. Exit")
        print("8. Query by pattern")
        print("9. Upsert")
        print("10. Batch upsert")
        print("11. Paginated query")
        print("12. Delete by username or phone")
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
            break
        elif choice == "8":
            search_by_pattern(conn)
        elif choice == "9":
            upsert(conn)
        elif choice == "10":
            batch_upsert(conn)
        elif choice == "11":
            paginated_query(conn)
        elif choice == "12":
            delete_by_field(conn)
        else:
            print("ERROR")
    conn.close()

if __name__ == "__main__":
    main()
