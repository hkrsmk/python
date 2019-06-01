import sqlite3
import sys

con = sqlite3.connect('test.db')
with con:
    try:
        cur = con.cursor()
        cur.execute('create table cars(id int, name text, price int)')
        #you can only create it once.

    except sqlite3.Error:
        print("Error")
        sys.exit(1)
