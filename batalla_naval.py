opcion,p = "",""
coordenadas = []
jugador1, jugador2 = [],[]
player = 0
visible1, visible2 = [],[]
victoria = 0

for i in range(0,10):
    visible1.append(["?","?","?","?","?","?","?","?","?","?"])
    visible2.append(["?","?","?","?","?","?","?","?","?","?"])

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
    p = input("ingrese donde quiere atacar: ")
    player = p.split(",")
    barcos = [1,2,3,4]

    global victoria1, victoria2
    victoria1,victoria2 = 0,0

    if "1"or "2"or "3" or "4" in koordinaten[int(player[1])][int(player[0])] :
        print("acertaste")
        if jugador == 1: 
            victoria1 += 1
            visible1[int(player[0])][int(player[1])] = "x"
            printear(visible1)
        else: 
            victoria2 += 1
            visible2[int(player[0])][int(player[1])] = "x"
            printear(visible2)

    else:
        print("fallaste")
        if jugador == 1: 
            visible1[int(player[0])][int(player[1])] = "0"
            printear(visible1)
        else: 
            visible2[int(player[0])][int(player[1])] = "0"
            printear(visible2)

    if jugador == 1: return victoria1 
    else: return victoria2
    
def jugar(coordinates):

    jugador1 = coordinates[0]
    jugador2 = coordinates[1]

    while True:
        victoria = jugador(jugador2,1)
        if victoria == 10:
            print("gano jugador 1")
            break

        victoria = jugador(jugador1,2)
        if victoria == 10:
            print("gano jugador 1")
            break

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
