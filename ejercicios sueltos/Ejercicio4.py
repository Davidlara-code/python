import random


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

