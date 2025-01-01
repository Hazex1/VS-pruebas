# APLICACION DE COMPRENSION DE LISTAS

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# Queremos tomar la lista de usuarios y
# aplicarles una transformación para que devuelva una lista de nombres

# Como se haría con for
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Otra forma mas elegante
# nombres = [expresion for item in items]

# nombres = [usuario[0] for usuario in usuarios] #map
# Filtrar - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# Sabiendo esto uno puede mezclar y realizar operaciones mas complejas como transformas y filtrar al mismo tiempo
# Siempre se debe filtra y luego la transformación
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# APLICACIÓN DE FILTER Y MAP

# nombres = list(map(lambda usuario: usuario[0], usuarios)) #aplicación de map

# menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
# print(menosUsuarios)
