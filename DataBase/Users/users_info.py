import sqlite3


def add_id_to_sql(user_id):
    conn = sqlite3.connect("DataBase/Users/users.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users_ids (id INTEGER PRIMARY KEY)''')

    try:
        cursor.execute("INSERT INTO users_ids (id) VALUES (?)", (user_id,))
    except sqlite3.IntegrityError:
        pass

    conn.commit()


def fetch_id_from_sql(user_id):
    conn = sqlite3.connect("DataBase/Users/users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id FROM users_ids WHERE id=?", (user_id,))
    except:
        cursor.execute('''CREATE TABLE IF NOT EXISTS users_ids (id INTEGER PRIMARY KEY)''')
        cursor.execute("SELECT id FROM users_ids WHERE id=?", (user_id,))

    result = cursor.fetchone()

    return result[0] if result else None
