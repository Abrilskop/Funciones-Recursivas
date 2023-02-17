# autor : Gianella Alexandra Ramos Ticahuanca
# fecha : 10/02/2023
# acción : Escribir un Programa que permita determinar el n-esimo término de la serie de Fibonacci de manera recursiva.

# Funcion Fibonacci
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Programa Pirncipal
num=int(input("Ingrese el numero: "))

# Calcular el n-esimo termino
fib=Fibonacci(num)

# Mostrar el resultado
print(f"El n-esimo termino del numero {num} es: ",fib)