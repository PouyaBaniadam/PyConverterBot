import sqlite3


def fetch_data_for_update_broadcast():
    conn = sqlite3.connect('C:\\Users\\Pouya\\Desktop\\PyConverterBot\\DataBase\\Users\\users.db')
    c = conn.cursor()
    c.execute('SELECT id FROM users_ids')
    users_ids = c.fetchall()
    conn.close()


    text = """
🆕 New update 🆕

What's new : 

🇮🇷 Persian language is now available. 🇮🇷

💻 All answers are in <code> MONO </code> mode. 💻

🗓️ Date section has been added. 🗓️

💵 Currency section has been added. 💵

🪲 Bug fixes. 🪲

                      🧑🏻‍💻 Powered by PouyaLj 🧑🏻‍💻

"""

    return users_ids, text
