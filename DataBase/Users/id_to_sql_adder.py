import sqlite3


def user_id_to_sql_adder(user_id):
    conn = sqlite3.connect("DataBase/Users/users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_ids (
        id INTEGER PRIMARY KEY,
        user_id INTEGER
    )
    """)

    cursor.execute("""
    INSERT INTO users_ids (user_id)
    VALUES (?)
    """, (user_id,))

    conn.commit()
