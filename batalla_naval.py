opcion,p = "",""
coordenadas = []
jugador1, jugador2 = [],[]
player = 0
visible1, visible2 = [],[]

visible1.append(["0","1","2","3","4","5","6","7","8","9","10"])
visible2.append(["0","1","2","3","4","5","6","7","8","9","10"])

for i in range(0,10):
    indice = str(i+1)
    visible1.append([indice,"_","_","_","_","_","_","_","_","_","_"])
    visible2.append([indice,"_","_","_","_","_","_","_","_","_","_"])

def printear(array):
    j = 0

    for j in range(len(array)):
        print(array[j])

def corde(path):

    archivo = open(path, encoding="utf16", errors="ignore")
    cont3 = 0
    lector = ""
    final=[]
    posc = []

    for cont3 in range(10):
        lector= archivo.readline()
        final.append(lector.split())

    return final

def cargar():

    entrada = ""
    posciciones = []
    cont2 = 0

    #loop para subir los archivos
    while True:
        print("por favor suba el archivo del jugador #",cont2+1)
        entrada = input()
        #use el try para 
        try:
            posciciones.append(corde(entrada))
            print("se ha subido de manera exitosa el archivo")
            cont2 += 1
            if cont2 == 2: break
        except FileNotFoundError:
            print("por favor vuelvalo a subir")

    print("gracias por subir los archivos, regresandolo al menu")
    return posciciones

def jugador(koordinaten,jugador):
    mensaje = "ingrese donde quiere atacar jugador #"+str(jugador)+": "
    p = input(mensaje)
    player = p.split(",")

    x = int(player[0])
    y = int(player[1])

    global victory
    victory = 0

    if "1" in koordinaten[y][x] or "2" in koordinaten[y][x] or "3" in koordinaten[y][x] or "4" in koordinaten[y][x]:
        print("acertaste")
        if jugador == 1: 
            victory += 1
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            victory += 1
            visible2[y][x] = "x"
            printear(visible2)

    else:
        print("fallaste")
        if jugador == 1: 
            visible1[y][x] = "0"
            printear(visible1)
        else: 
            visible2[y][x] = "0"
            printear(visible2)

    return victory
    
def jugar(coordinates):

    victoria1, victoria2 = 0,0
    victoria = 0

    jugador1 = coordinates[0]
    jugador2 = coordinates[1]

    while True:
        victoria = jugador(jugador2,1)
        if victoria == 1:
            victoria1 += 1
            if victoria1 == 12:
                print("gano el jugador #1")
            

        victoria = jugador(jugador1,2)
        if victoria == 1:
            victoria2 += 1
            if victoria1 == 12:
                print("gano el jugador #2")

while True:
    #menu de opciones
    print("Escoga una opcion")
    print("a)carga de archivos")
    print("b)jugar")
    print("c)terminar")
    
    opcion = input()

    if opcion == "a":
        coordenadas = cargar()

    elif opcion == "b":
        jugar(coordenadas)

    elif opcion == "c":
        break
    else:
        print("por favor ingrese una opcion valida")