# autor : Gianella Alexandra Ramos Ticahuanca
# fecha : 10/02/2023
# acción : Escribir un Programa que permita invertir el orden de los dígitos de un número entero positivo de manera recursiva.

# Funcion Invertir
def Invertir(n):
    inverso=0
    if n==0:
        return n
    else:
        n=n//10  # div
        residuo=n%10 # mod
        inverso=(inverso*10)+ residuo
    return Invertir(n)

# Programa Principal
num=int(input("Ingrese el numero: "))

# Calcular la inversion de los digitos del numero
inver=Invertir(num)

# Mostrar el resultado
print(f"El numero invertido es: ",inver)