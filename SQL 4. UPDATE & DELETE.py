__author__ = 'rudy'

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")

    c.execute("DELETE FROM employees WHERE firstname='Rik'")

    print "\nNew data:\n==============="

    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]


    c.execute("SELECT city, population from population WHERE state = 'CA'")
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]

