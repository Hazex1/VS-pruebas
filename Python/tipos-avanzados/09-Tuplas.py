# Una tupla es exactamente lo mismo que una lista, con una sutil diferencia. NO SE PUEDE CAMBIAR EN ABSOLUTO
# Se pueden crear nuevas tuplas pero no se pueden modificar

numeros = (1, 2, 3) + (4, 5, 6)  # Concatenación de tuplas
print(numeros)

# Queremos usar tuplas cuando queremos evitar la modificación de elementos

# La función recibe cualquier dato iterable y lo transforma en tupla
punto = tuple([1, 2])
print(punto)

# OPERACIONES CON TUPLAS
# Se pueden hacer todas las operaciones que se hacen en una lista excepto las que modifiquen las listas

menosnumeros = numeros[:2]
print(menosnumeros)

primero, segundo, *otros = numeros  # Desempaquetado de tuplas
print(primero, segundo, otros)

for n in numeros:  # Recorrerlas
    print(n)


# Como modificar tuplas

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
listaNumeros = tuple(listaNumeros)
print(listaNumeros)
