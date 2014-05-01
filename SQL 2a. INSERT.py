from ibus import exception

__author__ = 'rudy'

import sqlite3

employees = [
        ('De Volder', 'Rudy'),
        ('De Volder', 'Ilse'),
        ('Baeyens', 'Tom'),
        ('Op de Locht', 'Rik'),
        ('De Volder', 'Anja')
    ]

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    try:
        c.execute("CREATE TABLE employees(firstname, lastname)")
    except sqlite3.DatabaseError:
        print "Employees already exists"

    c.executemany("INSERT INTO employees(lastname, firstname) values (?, ?)",
                  employees)

    connection.commit()



