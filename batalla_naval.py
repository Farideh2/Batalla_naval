#se importa simpleaudioo para los sonidos
import simpleaudio as sa

#se inicializan algunas variables
opcion,p = "",""
coordenadas,ships = [],[]
jugador1, jugador2 = [],[]
player = 0
visible1, visible2 = [],[]

#se crean los objetos para los efectos de sonidos
explosion = "Explosion+9.wav"
explosionObj = sa.WaveObject.from_wave_file(explosion)

chapoteo = "Cannonball-Splash-A2-www.fesliyanstudios.com (online-audio-converter.com).wav"
chapoteoObj = sa.WaveObject.from_wave_file(chapoteo)

#aqui se declaran unas variables para crear los tableros visibles a los jugadores con coordenadas
visible1.append(["0","1","2","3","4","5","6","7","8","9","10"])
visible2.append(["0","1","2","3","4","5","6","7","8","9","10"])

#este for acaba de crear las variables visibles
for i in range(0,10):
    indice = str(i+1)
    visible1.append([indice,"_","_","_","_","_","_","_","_","_","_"])
    visible2.append([indice,"_","_","_","_","_","_","_","_","_","_"])

#en este for se imprimen las variables visibles y lo use tambien comno soporte durante la
#la crecacion del programa
def printear(array):
    j = 0

    for j in range(len(array)):
        print(array[j])

#este metodo decodifica los archivos
def corde(path):

    #se abren los archivos necesarios
    #en este caso se tiene que abrir en ambos formatos ya que puede variar
    archivo8 = open(path, encoding = "utf8")
    archivo = open(path ,encoding = "utf16", errors="ignore")

    #se declaran las variables necesarias
    lector = ""
    final=[]
    barcos = [0,0,0,0]
    checar = 0

    for cont3 in range(10):
        #se checa el formato de codificacion, para eso la primera vez se checa con el try
        #de la segunda vuelta en adelante ya lo lee en el formato correspondiente gracia a la variable checar
        #se lee linea por linea para saber cuantos barcos hay de cada numero
        if checar == 0:
            try:
                lector = archivo.readline()
                checar = 1
            except:
                lector = archivo8.readline()
                checar = 2
        elif checar ==1: lector = archivo.readline()
        else:lector = archivo8.readline()
        
        #se usa split para crear la linea en una matriz que luego se añade a la matriz final
        temp = lector.split()
        final.append(temp)

        #se checa cuantos barcos hay de cada numerop
        for l in range(len(temp)):
            if "1" in temp[l]:
                barcos[0] = barcos[0]+1
            if "2" in temp[l]:
                barcos[1] = barcos[1]+1
            if "3" in temp[l]:
                barcos[2] = barcos[2]+1
            if "4" in temp[l]:
                barcos[3] = barcos[3]+1
    return final, barcos

# se llama a este metodo cuando se necesita cargar los archivos
def cargar():

    entrada = ""
    posciciones = []
    cont2 = 0
    naves = []

    #loop para subir los archivos
    while True:
        print("por favor suba el archivo del jugador #",cont2+1)

        entrada = input()
        #use el try para saber si el archivo se pudo subir o no
        try:
            #corre el metodo que se usa para leer archivos
            temp = corde(entrada)
            posciciones.append(temp[0])
            naves.append(temp[1])
            print("se ha subido de manera exitosa el archivo")
            cont2 += 1
            if cont2 == 2: break
        except FileNotFoundError:
            print("por favor vuelvalo a subir")

    print("gracias por subir los archivos, regresandolo al menu")
    return posciciones,naves

#este metodo se corre cada vez que que los jugadrores quieran jugar y es donde se efectua el juego
def jugador(koordinaten,jugador, barcos):
    mensaje = "ingrese donde quiere atacar jugador #"+str(jugador)+": "
    p = input(mensaje)
    player = p.split(",")

    x = int(player[0])
    y = int(player[1])

    global victory
    victory = 0

    if visible1[y][x] == "0" or visible1[y][x] == "0":
        print("Esa coordenada ya se añadio")

    elif "1" in koordinaten[y-1][x-1] :
        print("Averiado")
        barcos[0] -= 1
        if jugador == 1: 
            visible1[y][x] = "x"
            printear(visible1)
        else: 
            visible2[y][x] = "x"
            printear(visible2)
        
        if barcos[0]== 0:
            print("Hundido")
            playExp = explosionObj.play()


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

    else:
        print("fallaste")
        if jugador == 1: 
            visible1[y][x] = "0"
            printear(visible1)
            playExp = chapoteoObj.play()
        else: 
            visible2[y][x] = "0"
            printear(visible2)
            playExp = chapoteoObj.play()
        
    print(barcos)
    return barcos

#este metodo prepara todo para el metodo principal(jugador)  
def jugar(coordinates, botes):

    #aqui se declaran cuantos barcos ahi de cada tipo y de que jugadores
    barcos1, barcos2 = botes[0],botes[1]

    #tambien se indica que  las matrizas y los jugadores a los que les pertenece
    jugador1 = coordinates[0]
    jugador2 = coordinates[1]

    #este metodo se mantiene verdadero hasta que un jugador gane
    #unnjugador gana una vez que se hundan todos los barcos, para eso se resta numeros de la matriz de barcos
    #cada vez que se averia uno hasta que llegue a cero
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
        coordenadas, ships = cargar()
    elif opcion == "b":
        jugar(coordenadas, ships)

    elif opcion == "c":
        break
    else:
        print("por favor ingrese una opcion valida")