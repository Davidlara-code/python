def select_all_tasks(conn):

    cur =conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows =cur.fetchall()

    for row in rows:
        print(row)