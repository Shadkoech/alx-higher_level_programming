#!/usr/bin/python3
""" Python module that lists all states
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # create a cursor object
    cur = db.cursor()

    # Execute the SQL query to select all states
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # Fetch all the selected rows by the query
    selected_rows = cur.fetchall()

    # Display the output
    for row in selected_rows:
        print(row)

    # close the cursor and database connection
    cur.close()
    db.close()
