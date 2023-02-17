# autor : Skop
# fecha : 10/02/2023
# acción : Escribir un Programa que determine el máximo común divisor de 2 números enteros positivos a, b de manera recursiva.

# Funcion Maximo
def Maximo(a,b):
    if b==0:
        return 0
    else:
        return Maximo(b,a % b)

# Programa Pirncipal
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

# Calcular el MCD de los 2 numeros
max=Maximo(num1,num2)

# Mostrar el resultado
print(f"El maximo como un divisor de {num1} y {num2} es: ",max)
