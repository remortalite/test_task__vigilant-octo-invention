import sqlite3


def create_table_links():
    conn = sqlite3.connect("mydb.sql")
    curs = conn.cursor()
    curs.execute(""" CREATE TABLE IF NOT EXISTS links
                     (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url VARCHAR(255) NOT NULL,
                        added_at DATETIME DEFAULT NOW
                     );
                     """)
    conn.commit()
    conn.close()

def select_links():
    conn = sqlite3.connect("mydb.sql")
    curs = conn.cursor()
    curs.execute("SELECT DISTINCT url FROM links")
    links = curs.fetchall()
    conn.close()
    return links or []
