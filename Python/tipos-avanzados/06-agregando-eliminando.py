mascotas = ["Wolfgang", "Pelusa", "Pulga",
            "Felipe", "Pulga", "Chanchito feliz"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("Pulga")  # Solo elimina la primera ocurrencia
mascotas.pop()  # Elimina el último elemento de la lista, si se le agrega un índice, se elimina el elemento a ese índice
del mascotas[0]  # Otra forma de eliminar elementos en la lista.
mascotas.clear()  # Se limpia completamente la lista
print(mascotas)
