mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
# Se puede acceder a cada elemento de la lista utilizando el [indice de elemento]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[:3])
print(mascotas[-1])
print(mascotas[1::2])  # Doble : implica saltos

numeros = list(range(21))
print(numeros[::2])
print(numeros[1::2])
