import sqlite3
from sqlite3 import Error

#Primero hay que conectarse a la tabla
def create_connection(my_BBDD):

    conn = None
    try:
        conn=sqlite3.connect(my_BBDD)
        return conn
    except Error as e :
        print('Error en la conexion',e)

    return conn 


def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)    


#  crear la funcion main para crear las tablas

def main():
    database = r"c:\Users\DAVID\Desktop\Postgrado\Ejercicios_Master_python\my_BBDD.db"

    sql_create_projects_table=""" CREATE TABLE IF NOT EXISTS projects(
                                    id integer primary key,
                                    nombre text,
                                    apellido text,
                                    direccion text
                                  );"""


    sql_create_tasks_table=""" CREATE TABLE IF NOT EXISTS tasks(
                                      id integer primary key,
                                      cif text
                                  );"""
                      
    conn= create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_projects_table)

        create_table(conn,sql_create_tasks_table)

    else:
        print("Error ")    











