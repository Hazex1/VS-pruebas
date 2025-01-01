def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

# Se transforma el parámetro de la función en un iterable recorrible por un for


suma(2, 5, 7)
suma(2, 5)
suma(2, 5, 54, 83)
