# SQLite ejercicio BBDD

import sqlite3
from sqlite3 import Error

def create_connection(mydatabase):

    conn=None

    try:
        conn=sqlite3.connect(mydatabase)
        print('CONEXION CORRECTA, version sqlite: ',sqlite3.version)
    except Error :
        print('Error en la conexion',Error)
    

print('hey')


def create_connection(mydatabase):

    conn=None

    try:
        conn=sqlite3.connect(mydatabase)
        print('CONEXION CORRECTA, version sqlite: ',sqlite3.version)
    except Error :
        print('Error en la conexion',Error)
    
    return conn

def create_table(conn,create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print('estoy en el cursor',e)  


def main():
    database=r"c:\Users\DAVID\Desktop\Postgrado\Ejercicios_Master_python\mydatabase.db"

    sql_create_projects_table=""" CREATE TABLE IF NOT EXISTS task(
                                   id integer primary key,
                                   name text not null,
                                   begin_date text,
                                   end_date text
                                    );"""

#----------------------------------
 
    conn=create_connection(database)

#VOY POR AQUI


    if conn is not None:
      create_table(conn, sql_create_projects_table)
      print('se creo la tabla')

    else:
      print("ERROR")    






