import sqlite3


def users_first_language(user_id):
    conn = sqlite3.connect("DataBase/Language/language.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_languages
    (
    user_id integer,
    language text
    )
    """)

    user = (user_id, "language_english")

    cursor.execute("SELECT * FROM users_languages WHERE user_id=?", (user_id,))
    result = cursor.fetchone()

    if not result:
        cursor.execute("""INSERT INTO users_languages VALUES (?,?)""", user)

    conn.commit()
    conn.close()


def user_language_update(user_id, language):
    conn = sqlite3.connect("DataBase/Language/language.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_languages
    (
    user_id integer,
    language text
    )
    """)

    user = (language, user_id)

    cursor.execute("""UPDATE users_languages SET language = ? WHERE user_id = ?""", user)
    conn.commit()
    conn.close()


def get_user_current_language(user_id):
    conn = sqlite3.connect("DataBase/Language/language.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT language FROM users_languages WHERE user_id = ?""", (user_id,))
    user_language = cursor.fetchone()

    conn.commit()
    conn.close()

    return user_language[0]
