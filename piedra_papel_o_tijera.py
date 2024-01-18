import random

letras_permitidas = ['r', 'p', 's']

def play():
    user = input("Cual es tu eleccion?? Elije una letra para jugar: \n 'r' para elegir PIEDRA \n 'p' por PAPEL \n 's' por TIJERA \n ")
    computer = random.choice(letras_permitidas)

    if user in letras_permitidas:
        if user == computer:
           print("Empate")
        elif is_win(user, computer):
            print("Ganaste!!")
        else:
            print("Perdiste!!!")
    else:
        print("Caracter no permitido")


    


def is_win(jugador, oponente):
    if(jugador == 'r' and oponente == 's') or (jugador == 'p' and oponente == 'r') or (jugador == 's' and oponente == 'p'):
        return True
    
booleano = True

while booleano:
    play()

    opccion = input("Aprieta cualquier tecla si quieres continuar con el juego \n Si quiere salir, presiona 'q': \n")

    if opccion =='q':
        break