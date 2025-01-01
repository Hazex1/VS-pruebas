# Devuelve True si and (True, True), or (True, False o False, True), not (Cambia el valor booleano al contrario)

gas = False
encendido = False
edad = 18

if gas and (encendido or edad > 17):
    print("puedes avanzar")
