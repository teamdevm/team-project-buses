import sqlite3


conn = sqlite3.connect("data/buses.db")
cur = conn.cursor()
with open("startup.sql") as startup_script:
    script_str = startup_script.read()
    cur.executescript(script_str)
    conn.commit()

conn.close()

