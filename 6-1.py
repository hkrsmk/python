import sqlite3 as lite
#'as lite' means that you'll always be calling sql, to avoid bugs

con = None
try:
    con = lite.connect('test.db')
    #connect to the database test.db

    cur = con.cursor()
    #lets you know where you are

    cur.execute('SELECT SQLITE_VERSION()')
    #execute a command using the cursor

    data = cur.fetchone()
    #fetchall to get all data

    print("SQLite version: %s" % data)

except lite.Error:
    print("Error!")

#didn't catch the end part. However, you can also
#use 'with' syntax so that python will close the file for you
