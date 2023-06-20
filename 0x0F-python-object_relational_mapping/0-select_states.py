#!/usr/bin/python3
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]

# Create a connection
conn = MySQLdb.connect(
    host="localhost", user=username, passwd=password, port=3306, db=dbname)

# Create a cursor
cursor = conn.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
conn.close()
