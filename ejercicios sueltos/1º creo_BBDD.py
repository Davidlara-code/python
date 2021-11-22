# SQLite ejercicio BBDD

import sqlite3
from sqlite3 import Error

def create_connection(my_BBDD):

    conn=None

    try:
        conn=sqlite3.connect(my_BBDD)
        print('CONEXION CORRECTA, version sqlite: ',sqlite3.version)
    except Error :
        print('Error en la conexion',Error)

    finally:
        if conn:
            conn.close()    


if __name__=='__main__':
    create_connection(r"c:\Users\DAVID\Desktop\Postgrado\Ejercicios_Master_python\my_BBDD.db")


