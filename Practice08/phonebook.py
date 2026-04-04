import psycopg2
from config import load_config


# ================== CONNECTION ==================
def get_conn():
    return psycopg2.connect(**load_config())


# ================== TABLE ==================
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL
    )
    """

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()

    print("✅ Table 'phonebook' ready in phonebook_db")


# ================== UPSERT ==================
def upsert_user():
    name = input("👤 Name: ")
    surname = input("👤 Surname: ")
    phone = input("📞 Phone: ")

    query = "CALL upsert_user(%s, %s, %s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, surname, phone))
        conn.commit()

    print("✅ User added/updated")


# ================== BULK INSERT ==================
def insert_many():
    print("👥 Enter names:")
    names = input().split()

    print("👥 Enter surnames:")
    surnames = input().split()

    print("📞 Enter phones:")
    phones = input().split()

    if not (len(names) == len(surnames) == len(phones)):
        print("❌ Sizes do not match")
        return

    query = "CALL insert_many_users(%s, %s, %s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (names, surnames, phones))
        conn.commit()

    print("✅ Bulk insert done")


# ================== SEARCH ==================
def search_contacts():
    pattern = input("🔍 Search: ")

    query = "SELECT * FROM search_phonebook(%s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (pattern,))
            rows = cur.fetchall()

    print_contacts(rows)


# ================== PAGINATION ==================
def pagination():
    try:
        limit = int(input("📄 Limit: "))
        offset = int(input("➡️ Offset: "))
    except ValueError:
        print("❌ Numbers only")
        return

    query = "SELECT * FROM get_phonebook_paginated(%s, %s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit, offset))
            rows = cur.fetchall()

    print_contacts(rows)


# ================== DELETE ==================
def delete_contact():
    value = input("❌ Enter name/surname/phone: ")

    query = "CALL delete_user(%s)"

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (value,))
        conn.commit()

    print("🗑 Deleted")


# ================== DISPLAY ==================
def print_contacts(rows):
    if not rows:
        print("❌ No data")
        return

    print("\n📋 CONTACTS:")
    print("-" * 40)

    for r in rows:
        print(f"Name: {r[0]} | Surname: {r[1]} | Phone: {r[2]}")

    print("-" * 40)


# ================== MENU ==================
def main():
    print("🔌 Connecting to database: phonebook_db")
    create_table()

    while True:
        print("\n📱 PHONEBOOK MENU")
        print("1 - Upsert user")
        print("2 - Insert many")
        print("3 - Search")
        print("4 - Pagination")
        print("5 - Delete")
        print("0 - Exit")

        choice = input("\n👉 Choose: ")

        if choice == "1":
            upsert_user()
        elif choice == "2":
            insert_many()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()