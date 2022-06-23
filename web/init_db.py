import sqlite3
from os.path import exists
from os import remove as rm
from glob import glob
from models import db_filename


conn = sqlite3.connect(db_filename)
cur = conn.cursor()
try:
    cur.execute("SELECT * FROM db_ver LIMIT 1;")
    ver = int(cur.fetchall()[0][0])
except:
    ver = 0

delete = False
max_ver = len(glob("sql/migrate*.sql"))
print(f"Current db version is {ver}, the latest version is {max_ver}")
for cur_ver in range(ver + 1, max_ver + 1):
    with open(f"sql/migrate{cur_ver}.sql") as startup_script:
        try:
            script_str = startup_script.read()
            cur.executescript(script_str)
            cur.execute(f"UPDATE db_ver SET db_ver = {cur_ver}")
            conn.commit()
            print(f"Updated to version {cur_ver}")
        except sqlite3.OperationalError as ex:
            if ver == 0 and "syntax error" in str(ex):
                print("SQL syntax error:", ex)
                delete = True
            break

conn.close()
if delete:
    rm(db_filename)
    print("Database file deleted")
