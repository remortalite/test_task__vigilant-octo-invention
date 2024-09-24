import sqlite3


conn = sqlite3.connect("mydb.sql")

def create_table_links():
    curs = conn.cursor()
    curs.execute(""" CREATE TABLE IF NOT EXISTS links
                     (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url VARCHAR(255) NOT NULL,
                        added_at DATETIME DEFAULT NOW
                     );
                     """)
    conn.commit()
