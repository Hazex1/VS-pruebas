# iterar lista de elementos
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No está el número :(")

for char in "Ultimate python":
    print(char)
