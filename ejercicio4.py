# autor : Skop
# fecha : 19/02/2023
# acción : Escribir un Programa que permita invertir el orden de los dígitos de un número entero positivo de manera recursiva.

# Funcion Invertir
def Invertir(n):
    if n < 10:
        return n
    else:
      ultimo_digito = n % 10
      numero_restante = n // 10
      return int(str(ultimo_digito) + str(Invertir(numero_restante)))

# Programa Principal
num=int(input("Ingrese el numero: "))

# Calcular la inversion de los digitos del numero
inver=Invertir(num)

# Mostrar el resultado
print(f"El numero invertido es: ",inver)
