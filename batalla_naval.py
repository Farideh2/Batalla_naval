opcion = ""


def cordenadas(path):

    archivo = open(path, encoding="utf16", errors="ignore")
    cont3 = 0
    lector = ""
    final=[]

    lector = archivo.read()
    final = lector.split()
    
    barco, barco2, barco3, barco4 = [],[],[],[]

    for cont3 in range(len(final)):

        y = 0
        x = 0

        y = int(cont3/10)
        x = int(round(((cont3/10)-y)*10))

        if final[cont3]=="1":
            barco.append([x+1,y+1])
        elif final[cont3]=="2":
            barco2.append([x+1,y+1])
        elif final[cont3]=="3":
            barco3.append([x+1,y+1])
        if final[cont3]=="4":
            print(x+1,y+1)
            barco4.append([x+1,y+1])


    return barco, barco2,barco3,barco4


def cargar():
    entrada = ""
    posciciones = [[],[]]
    cont2 = 0
    for cont in range(0,2):
        print("por favor suba el archivo del jugador #",cont+1)
        entrada = input()
        posciciones[cont]=cordenadas(entrada)
        print(posciciones[cont][cont2])
        print("se ha subido de manera exitosa el archivo")
    print("gracias por subir los archivos, regresandolo al menu")

def jugar():
    print("ya estan jugando")


while True:

    print("Escoga una opcion")
    print("a)carga de archivos")
    print("b)jugar")
    print("c)terminar")
    
    opcion = input()

    if opcion == "a":
        cargar()
    elif opcion == "b":
        jugar()
    elif opcion == "c":
        break
    else:
        print("por favor ingrese una opcion valida")
