
#aqui tenemos el problema de que si le pongo el 2 no llega
#al 2 se queda en el 1 por que cuenta el 0,
#tendria que meter numero+=1 para que llegara al numero 2
# o eso es lo que entiendo yo en el ejercicio.
numero=int(input("dame un numero"))
numero+=1
for numero in range(0,numero):
  print (f"estos son los numeros {numero}")



  #DICCIONARIO

  casa={"salon":"mesa",
  "cocina":"nevera",
  "dormitorio":"cama",
  "baño":"ducha"
  }

for key,value in casa.items():
    print(key,value)

