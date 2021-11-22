import random

'''
Escribe una función que acepte dos variables numéricas y calcule la suma y la 
resta de dichas cifras. La función devolverá tanto la suma como la resta. 
Utiliza las excepciones para controlar algún posible error dentro de la función.

'''
#aqui podria meter un while para que se repitiese toda la funcion 
#en caso de meter algun dato que no fuera un entero y saltara la excepcion.

def funcion():
    
       try:
         numero1=int(input("dame el primer numero"))
         numero2=int(input("dame el segundo numero"))
         suma=numero1+numero2
         resta=numero1-numero2
         return [suma,resta]
       except ValueError:
         print("por favor solo ingrese numeros")


print(funcion())

#FUNCION RECURSIVA
'''
Escriba una función recursiva para calcular la suma de números del 0 al 10. 
El resultado final ha de ser 55
'''
def recursiva(x):
    
    if x==55:
        print(f"RESULTADO FINAL ES: " , x)
    else:    
        print(f"vamos por este numero: " , x)
        return  recursiva(x +1)




aleatorio1=random.randint(0,10)
aleatorio2=random.randint(0,10)

recursiva(aleatorio1+aleatorio2)

