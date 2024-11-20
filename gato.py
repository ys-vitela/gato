import os
import time

def clear():
    if os.name == "posix":
        os.system ("clear")
    else:
        os.system ("cls")
    
def gatito(posicion):
    print("\n")
    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}  ".format(posicion[0], posicion[1], posicion[2]))
    print("\t_____|_____|_____")
    
    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}  ".format(posicion[3], posicion[4], posicion[5]))
    print("\t_____|_____|_____")
    
    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}  ".format(posicion[6], posicion[7], posicion[8]))
    print("\t     |     |     ")

def empate(x, o):
    if (x+o==9):
        return True
    return False

def victoria(posicion):
    posibles_victorias=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in posibles_victorias:
        contador_x=0
        contador_o=0
        for j in i:
            if posicion[j-1]=="X":
                contador_x+=1
            elif posicion[j-1]=="O":
                contador_o+=1
            if contador_x==3 or contador_o==3:
                return True
    return False
                

def juego(player1, player2, diccionario, posicion, actual):
    cant_x=0
    cant_o=0
    while True:
        clear()
        gatito(posicion)
        
        if empate(cant_x, cant_o):
            print("Juego Empatado")
            exit()
        if victoria(posicion):
            print("Ganador: "+ anterior)
            exit()
            
        print("\n"+actual+" En que casilla deseas jugar (1-9): ")
        try:
            casilla=int(input())
        except:
            print("Elige un numero")
            continue
        if casilla<1 or casilla>9:
            print("Casilla fuera de rango")
            time.sleep(2)
            continue
        
        if posicion[casilla-1]!=" ":
            print("Casilla ocupada, elige una vacía")
            continue
        elif posicion[casilla-1]==" ":
            posicion[casilla-1]=diccionario.get(actual)
            if diccionario.get(actual)=="X":
                cant_x+=1
            elif diccionario.get(actual)=="O":
                cant_o+=1
        
        if actual==player1:
            actual=player2
            anterior=player1
        else:
            actual=player1
            anterior=player2

def main():
    print("Bienvenido al juego Tic Tac Toe\n")

    player1=input("\nIngrese el nombre del jugador 1: ")
    player2=input("\nIngrese el nombre del jugador 2: ")
    
    posicion=[" " for i in range(9)]
    gatito(posicion)
    
    print("""
          {}
          Elige con que deseas jugar
          1.- Jugar con X
          2.- Jugar con O
          3.- Salir
          """.format(player1))
    try:
        opcion=int(input("Ingresa la opción deseada: "))
    except:
        print("Opción inválida, reinicia el juego y elige un numero")
        exit()
    
    if opcion==1:
        diccionario={
            player1: "X",
            player2: "O",
        }
    elif opcion==2:
        diccionario={
            player1: "O",
            player2: "X",
        }
    elif opcion==3:
        print("\nGracias por usar el programa :D")
        exit()
    else:
        print("Opción inválida, aprende a leer perro")
        exit()

    juego(player1, player2, diccionario, posicion, actual=player1)
    

if __name__=="__main__":
    main()