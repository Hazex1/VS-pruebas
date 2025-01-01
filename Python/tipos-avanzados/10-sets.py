# set significa grupo o conjunto
# Un set es una coleccion de datos que no se puede repetir y que tampoco está ordenada

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)  # Tambien se pueden setear las tuplas

# OPERADORES INTERESANTES DE SET

# print(primer | segundo) #Genera una UNION de los elementos y eliminará los duplicados
# print(primer & segundo)  # Genera una INTERSECCION de los elementos
# print(primer - segundo)  # Genera una DIFERENCIA de los elementos, muestra los datso del conjuntos de la izquierda pero elimina los que están en la derecha en el primer grupo
# Genera una DIFERENCIA SIMETRICA, devuelve los elementos que estén en el primer y segundo pero que no se encuentren en ambos.
# print(primer ^ segundo)

# No permite datos repetidos o duplicados.
# Los set se pueden trabajar muy similar como se trabajan las listas

# no se puede acceder a los elementos de los sets, se puede buscar en los elementos

if 5 in segundo:
    print("hola mundo")
