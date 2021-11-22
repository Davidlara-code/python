class calculadora:
   

    def  __init__  (self,mi_num1,mi_num2):
        self.num1=mi_num1
        self.num2=mi_num2

   

    #metodos  que hace el objeto(funciones)
    def sumar(self):
        suma=self.num1 + self.num2
        print("esta es la suma", suma )

    def restar(self):
        resta=self.num1 - self.num2
        print("esta es la resta", resta )
    
    def multiplicar(self):
        multiplicacion=self.num1 * self.num2
        print("esta es la multiplicacion", multiplicacion )

    def dividir(self):
        division=self.num1 / self.num2    
        print("esta es la division", division )


# aqui lo pruebo
c=calculadora(2,5)

c.sumar()
c.restar()
c.multiplicar()
c.dividir()