import simpleaudio as sa

opcion,p = "",""
coordenadas = []
jugador1, jugador2 = [],[]
player = 0
visible1, visible2 = [],[]

explosion = "Explosion+9.wav"
explosionObj = sa.WaveObject.from_wave_file(explosion)

chapoteo = "Cannonball-Splash-A2-www.fesliyanstudios.com (online-audio-converter.com).wav"
chapoteoObj = sa.WaveObject.from_wave_file(chapoteo)

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
    lector = ""
    final=[]

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

def jugador(koordinaten,jugador, barcos):
    mensaje = "ingrese donde quiere atacar jugador #"+str(jugador)+": "
    p = input(mensaje)
    player = p.split(",")

    x = int(player[0])
    y = int(player[1])

    global victory
    victory = 0

    if "1" in koordinaten[y-1][x-1] :
        print("acertaste")
        barcos[0] -= 1
        if jugador == 1: 
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            visible2[y][x] = "x"
            printear(visible2)
        
        if barcos[0]== 0:
            print("hundiste el barco 1")
            playExp = explosionObj.play()
            playExp.wait_done()

    elif "2" in koordinaten[y-1][x-1]:
        print("acertaste")
        barcos[1] -= 1
        if jugador == 1: 
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            visible2[y][x] = "x"
            printear(visible2)
        
        if barcos[1]== 0:
            print("hundiste el barco 2")
            playExp = explosionObj.play()
            playExp.wait_done()

    elif "3" in koordinaten[y-1][x-1]:
        print("acertaste")
        barcos[2] -= 1
        if jugador == 1: 
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            visible2[y][x] = "x"
            printear(visible2)
        
        if barcos[2]== 0:
            print("hundiste el barco 3")
            playExp = explosionObj.play()
            playExp.wait_done()
        
    elif "4" in koordinaten[y-1][x-1]:
        print("acertaste")
        barcos[3] -= 1
        if jugador == 1: 
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            visible2[y][x] = "x"
            printear(visible2)
        
        if barcos[3]== 0:
            print("hundiste el barco 4")
            playExp = explosionObj.play()
            playExp.wait_done()

    else:
        print("fallaste")
        if jugador == 1: 
            visible1[y][x] = "0"
            printear(visible1)
            playExp = chapoteoObj.play()
            playExp.wait_done()
        else: 
            visible2[y][x] = "0"
            printear(visible2)
            playExp = chapoteoObj.play()
            playExp.wait_done()
        

    return barcos
    
def jugar(coordinates):

    barcos1, barcos2 = [2,3,4,5],[2,3,4,5]

    jugador1 = coordinates[0]
    jugador2 = coordinates[1]

    while True:
        victoria1 = jugador(jugador2,1, barcos1)
        if sum(victoria1) == 0:
            print("gano el jugador 1")
            break

        victoria2 = jugador(jugador1,2, barcos2)
        if sum(victoria2) == 0:
            print("gano el jugador 1")
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