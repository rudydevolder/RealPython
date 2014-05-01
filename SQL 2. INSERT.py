__author__ = 'rudy'

import sqlite3
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
    #cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)") # => Error

    conn.commit()

except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again..."
    print "Database error : ", sqlite3.DatabaseError

#Close the database:
conn.close()

