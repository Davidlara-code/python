import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

"""
def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()

con = sql_connection()

sql_table(con)
"""
def select_all_tasks(conn):

    cur =conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows =cur.fetchall()

    for row in rows:
        print(row)


