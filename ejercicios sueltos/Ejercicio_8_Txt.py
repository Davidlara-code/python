# ESTO ES LECTURA
f = open('ejemplo.txt', 'w')

f.write("CU CU DRU LU\n")

# meto mas datos
f = open('ejemplo.txt', 'a')

f.write("SEGUNDA LINEA\n")


f.close()

# ESTO ES LEER

f = open('ejemplo.txt', 'r')


informacion = f.read()

print(informacion)

f.close()







