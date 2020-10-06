opcion = ""

def cargar():
    for cont in range(0,2):
        print("por favor suba el archivo del jugador #",cont+1)
        print("se ha subido de manera exitosa el archivo")
    print("gracias por subir los archivos, regresandolo al menu")

def jugar():
    print("ya estan jugando")


while True:
    opcion = input()

    print("Escoga una opcion")
    print("a)carga de archivos")
    print("b)jugar")
    print("c)terminar")

    if opcion == "a":
        cargar()
    elif opcion == "b":
        jugar()
    elif opcion == "c":
        break
    else:
        print("por favor ingrese una opcion valida")
