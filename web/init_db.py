import sqlite3
from os.path import exists
from glob import glob


conn = sqlite3.connect("data/buses.db")
cur = conn.cursor()
try:
    cur.execute("SELECT * FROM db_ver LIMIT 1;")
    ver = int(cur.fetchall()[0][0])
except:
    ver = 0

max_ver = len(glob("sql/migrate*.sql"))
print(f"Current db version is {ver}, maximum version is {max_ver}")
for cur_ver in range(ver + 1, max_ver + 1):
    with open(f"sql/migrate{cur_ver}.sql") as startup_script:
        script_str = startup_script.read()
        cur.executescript(script_str)
        cur.execute(f"UPDATE db_ver SET db_ver = {ver + 1}")
        conn.commit()
        print(f"Updated to version {cur_ver}")

conn.close()

