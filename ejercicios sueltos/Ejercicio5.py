import random
#LISTA
'''
Utiliza una lista para almacenar los números del 1 al 10 la cual debe ser rellenada 
con el uso de un bucle while. Finalmente muestra la lista en orden inverso.'''

contador=0
numeros=[]
while contador <10:
    aleatorio=random.randint(0,10)
    numeros.append(aleatorio)
    
    contador+=1

numeros.sort(reverse=True)

print(numeros)


#DICCIONARIO
'''
1. Crea un diccionario con 4 valores.
2. Muestra los valores del diccionario.
3. Modifica el 3º valor del diccionario
4. Añade un nuevo valor al diccionario de tipo lista
5. Muestra nuevamente los valores '''

larousse={"harry":"magia",
"espacio":"strange",
"capitan":"escudo",
"Malaga":"playa"
}
#MUESTRO LOS VALORES
for clave,valor in larousse.items():
    print(clave,valor)

print("*************************************************")
#MODIFICO 3º VALOR ---> "capitan":"escudo" <----

larousse['capitan']='VALOR CAMBIADO'


for clave,valor in larousse.items():
    print(clave,valor)

print("*************************************************")
#añadir nuevo valor

larousse["CLAVE NUEVA"]="VALOR NUEVO"

#LO SACO POR CONSOLA
for clave,valor in larousse.items():
    print(clave,valor)