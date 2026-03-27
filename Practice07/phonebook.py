import psycopg2
import csv

# --- CONFIG ---
config = {
    "host": "localhost",
    "database": "phonebook_db",
    "user": "postgres",
    "password": "Aizere2008"
}

# --- CONNECT ---
def connect():
    try:
        conn = psycopg2.connect(**config)
        return conn
    except Exception as e:
        print("Connection error:", e)

# --- CREATE TABLE ---
def create_table(cur, conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)
    conn.commit()

# --- INSERT FROM CSV ---
def insert_from_csv(cur, conn):
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )

        conn.commit()
        print("CSV data inserted successfully")
    except Exception as e:
        print("Error:", e)

# --- INSERT FROM CONSOLE ---
def insert_manual(cur, conn):
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact added")

# --- QUERY ---
def query_contacts(cur):
    print("1 - Show all")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":
        cur.execute("SELECT * FROM contacts")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "3":
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    print("\n--- RESULTS ---")
    for row in rows:
        print(row)

# --- UPDATE ---
def update_contact(cur, conn):
    name = input("Enter name to update: ")
    new_name = input("New name (or press enter to skip): ")
    new_phone = input("New phone (or press enter to skip): ")

    if new_name:
        cur.execute(
            "UPDATE contacts SET name=%s WHERE name=%s",
            (new_name, name)
        )

    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s",
            (new_phone, name)
        )

    conn.commit()
    print("Updated successfully")

# --- DELETE ---
def delete_contact(cur, conn):
    print("1 - Delete by name")
    print("2 - Delete by phone")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))

    conn.commit()
    print("Deleted successfully")

# --- MAIN MENU ---
def main():
    conn = connect()
    cur = conn.cursor()

    create_table(cur, conn)

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1 - Insert from CSV")
        print("2 - Add contact")
        print("3 - Query contacts")
        print("4 - Update contact")
        print("5 - Delete contact")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_from_csv(cur, conn)

        elif choice == "2":
            insert_manual(cur, conn)

        elif choice == "3":
            query_contacts(cur)

        elif choice == "4":
            update_contact(cur, conn)

        elif choice == "5":
            delete_contact(cur, conn)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    cur.close()
    conn.close()

# --- RUN ---
if __name__ == "__main__":
    main()