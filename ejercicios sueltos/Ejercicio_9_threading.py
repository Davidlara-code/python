import threading


def Thread_execution(n, s):
    numeros = n

    while numeros < 10:
        print(" soy el PRIMERO :  ", numeros)
        print("soy el SEGUNDO : ", numeros)

        numeros += 1


primero = threading.Thread(target=Thread_execution, args=(1, 'hilo1'))

segundo = threading.Thread(target=Thread_execution, args=(1, 'hilo2'))


primero.start()

segundo.start()
