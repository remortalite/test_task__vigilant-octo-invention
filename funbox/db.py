import sqlite3


def create_table_links():
    conn = sqlite3.connect("mydb.sql")
    curs = conn.cursor()
    curs.execute(""" CREATE TABLE IF NOT EXISTS links
                     (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url VARCHAR(255) NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                     );
                     """)
    conn.commit()
    conn.close()

def select_links(start=None, end=None):
    conn = sqlite3.connect("mydb.sql")
    curs = conn.cursor()

    sql = """
        SELECT DISTINCT url
        FROM links
        WHERE created_at BETWEEN (?) and (?)
    """

    if start:
        start_expr = "created_at >= (?)"
    if end:
        end_expr = "created_at < (?)"
    curs.execute(sql, (start, end))
    links = tuple(map(lambda x: x[0], curs.fetchall()))
    conn.close()
    return links or []

def save_links(links):
    conn = sqlite3.connect("mydb.sql")
    curs = conn.cursor()
    curs.executemany("INSERT INTO links (url) VALUES (?)", list(links))
    conn.commit()
    conn.close()
