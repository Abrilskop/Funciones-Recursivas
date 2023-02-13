# autor : Gianella Alexandra Ramos Ticahuanca
# fecha : 29/05/2023
# acción : Escribir un Programa que calcule la potencia de un numero entero positivo (a)elevado a un exponente entero positivo ( b) de manera recursiva.

# Funcion Potencia
def potencia(b,e):
    if b==0:
        return b
    else:
        return potencia(e%b)

# Programa Pirncipal
base=int(input("Ingrese el numero base: "))
exponente=int(input("Ingrese el Exponente: "))

#Calcula la potencia
pot=potencia(base,exponente)

# Mostrar el resultado
print(f"La potencia del numero {base} es: ",pot)