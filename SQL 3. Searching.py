__author__ = 'rudy'

import sqlite3

with sqlite3.connect("new.db") as connection:

    c = connection.cursor()
    for row in c.execute("SELECT firstname, lastname from employees"):
        print row   # Notice output of the 'u' character
    print "==========================================================="
    # Now store all fetches in tuples:
    c.execute("SELECT firstname, lastname from employees")
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]




