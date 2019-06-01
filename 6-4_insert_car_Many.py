#allow multiple car import repeatedly. (remove # from line of code below)
#also, run command to check on car

import sqlite3
import sys
con = sqlite3.connect('test.db')
pricefrom = input("Check on cars more than how much?")
sql = 'select name, price from cars where price >={}'.format(pricefrom)

with con:
    try:
        cur = con.cursor()
        
        sqlInsertMany = """
            insert into cars values(11, "A", 123);
            insert into cars values(33,"B",123);
            insert into cars values(3, "C", 123);
            """
            
        #cur.executescript(sqlInsertMany)
        
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error:
        print("Error ")
        sys.exit(1)
