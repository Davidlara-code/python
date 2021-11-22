
import sqlite3

from sqlite3 import Error


con = sqlite3.connect('my_BBDD.db')


def sql_connection():

    try:

        con = sqlite3.connect('my_BBDD.db')

        return con

    except Error:

        print(Error)


def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employee(id integer PRIMARY KEY, name text, direccion text, telefono real)")
    cursorObj.execute("CREATE TABLE departament(id integer , name text)")
    con.commit()


con = sql_connection()

sql_table(con)


def sql_insert(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO employee VALUES(1, 'John', 'calle el roble.6 Madrid', 7234567)")
    cursorObj.execute("INSERT INTO departament VALUES(1, 'David')")
    con.commit()


con = sql_connection()

sql_insert(con)


def sql_update(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employee SET name = "Rodrigo" where id = 1')
    cursorObj.execute('UPDATE departament SET name = "Alberto" where id = 1')
    con.commit()


sql_update(con)

# entiendo que listar es preguntar por todas las tablas que tiene mi bbdd


def listar(con):

    cursorObj = con.cursor()
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())


listar(con)


print('CONSULTAR DATOS DE TODOS LOS REGISTROS')


def consultar_todos_los_datos(con):

    cursorObj = con.cursor()

    cursorObj.execute("SELECT * FROM departament")

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


consultar_todos_los_datos(con)


print('AHORA BORRO LOS REGISTROS DE LA TABLA')


def delete_datos(con):

    sql = 'DELETE FROM departament'

    cursorObj = con.cursor()

    cursorObj.execute(sql)

    con.commit()

    

delete_datos(con)

consultar_todos_los_datos(con)


