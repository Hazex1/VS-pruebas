# los diccionarios son una coleccion de datos que se encuentran organizados en formato llave:valor
# Los diccionarios son sumamente utilizados

# Solo acepta strings como llave pero lo de la derecha puede ser cualquier cosa
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  # Agregar otra llave
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontré lala", punto["lala"])

# METODO GET DE LOS DICCIONARIOS

print(punto.get("x"))
print(punto.get("lala", 97))  # Devuelve none o un valor que yo quiera (97)
# Eliminar llaves

del punto["x"]
del (punto["y"])

print(punto)

# ACCEDER A LOS DICCIONARIOS
punto["x"] = 25
for valor in punto:  # Recorre las llaves
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# USO REALISTA DE DICCIONARIOS

usuarios = [
    {"id": 1, "nombre": "Chanchito"}, {
        "id": 2, "nombre": "Feliz"}, {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])  # Se rescatan todos los usuarios
