
# primero importo sqlite

import sqlite3

#creo el archivo donde se almacenara mi base de datos

con = sqlite3.connect('mydatabase.db')

#creo el cursor para para llamar al método execute () para ejecutar cualquier consulta SQL

cursorObj = con.cursor()

