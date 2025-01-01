numeros = [2, 5, 4, 45, 75, 22]

# numeros.sort() #Ordenar normal
# numeros.sort(reverse=True) #ordenar al revés
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# La diferencia entre sort y sorted es que el primero cambia la variable

usuarios = [["Chanchito", 4], ["Aelipe", 1], ["Dulga", 5]]

# Esta función permite ordenar mediante el sort utilizando la función como key
# def ordena(elemento):
#     return elemento[1]

# Lamda ahorra tener que generar una función def ordena, lamda corresponde a una función anónima.
# Las funciones anónimas se suelen utilizar una única vez.
usuarios.sort(key=lambda el: el[1], reverse=False)
print(usuarios)
