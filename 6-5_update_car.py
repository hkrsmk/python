#update data

import sqlite3
import sys
con = sqlite3.connect('test.db')

with con:
    try:
        cur = con.cursor()
        sqlPrint = "select * from cars" 
        cur.execute(sqlPrint)
        rows = cur.fetchall()
        for row in rows:
            print(row)
            
        carname = input("Amend which car?")
        #must put the name into quotation marks.
        #for integers, you will not need the quotation marks.
        
        carprice = input("New price?")
        
        sql = "update cars set price={1} where name={0}".format(carname, carprice)
        cur.execute(sql)

        cur.execute(sqlPrint)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
    except sqlite3.Error:
        print("Error ")
        sys.exit(1)
