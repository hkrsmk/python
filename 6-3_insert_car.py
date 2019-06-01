import sqlite3
import sys

con = sqlite3.connect('test.db')
with con:
    try:
        cur = con.cursor()
        #cur.execute('delete from cars where 1')
        
        cur.execute('insert into cars values (1, "Audi", 84938)')
        #if you use '' inside, then outside should use ""
        
        cur.execute('select * from cars')
        rows = cur.fetchall()
        
        for row in rows:
            print(row)

    except sqlite3.Error:
        print("Error")
        sys.exit(1)
