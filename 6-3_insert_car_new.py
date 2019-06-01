#allow car import repeatedly.

import sqlite3
import sys
con = sqlite3.connect('test.db')

while True:
    print("Insert new car")
    carid = input("Car id?")
    carName = input("Brand?")
    carPrice = input("Price?")

    with con:
        try:
            cur = con.cursor()
            #cur.execute('delete from cars where 1')

            sql = 'insert into cars values ({}, "{}", {})'.format(carid,carName,carPrice)
            
            cur.execute(sql)
            #if you use '' inside, then outside should use ""
            
            cur.execute('select * from cars')
            rows = cur.fetchall()
            
            for row in rows:
                print(row)

        except sqlite3.Error:
            print("Error")
            sys.exit(1)
