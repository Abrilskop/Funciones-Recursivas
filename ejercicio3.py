# autor : Gianella Alexandra Ramos Ticahuanca
# fecha : 10/02/2023
# acción : Escribir un Programa que permita determinar el n-esimo término de la serie de Fibonacci de manera recursiva.

# Funcion Fibonacci
def Fibonacci(a,b):
    if n <= 1:
        return n
 
    return fib(n - 1) + fib(n - 2)

# Programa Pirncipal
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

# Calcular el n-esimo termino
max=Maximo(num1,num2)

# Mostrar el resultado
print(f"El maximo como un divisor de {num1} y {num2} es: ",max)