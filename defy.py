import os
import time

tab = [1,2,3,4,5,6,7,8,9]
liczbaRuchów = 0
name1 = input
name2 = input

def gameBoard():
    print (" |",tab[0],"|",tab[1],"|",tab[2],"|\n",
    "|",tab[3],"|",tab[4],"|",tab[5],"|\n",
    "|",tab[6],"|",tab[7],"|",tab[8],"|",)
def circleMove():
    gameBoard()
    print (tab)
    circle = int(input("Teraz kółko: "))
    tab[circle-1] = 'O'
def crossMove():
    gameBoard()
    cross = int(input("Teraz krzyżyk: "))
    tab[cross-1] = 'X'
def startScreen():
    print("Witamy w SUPER GRZE !!!\n\nWprowadź gracza grającego kółkami:\n")
    name1=input()
    print("\nWitaj "+name1+"!\n"+"\nZ kim chcesz zagrac?\n\nWprowadz gracza grającego krzyżykami:\n")
    name2=input()
    while(name2 == name1):
        print ("Ta nazwa jest już zajęta, spróbuj ponownie: ")
        name2=input()
    print("\nWitaj "+name2+"!\n"+"\nAle masz szczescie!! Zagrasz z "+
        name1+"\n\nPOWODZENIA!\nZACZYNA",name1)
    time.sleep(2)
    os.system('clear')
def win():
    if (tab[0]==tab[1]==tab[2]) or (tab[3]==tab[4]==tab[5]) or (tab[6]==tab[7]==tab[8]) or (tab[0]==tab[3]==tab[6]) or (tab[2]==tab[5]==tab[8]) or(tab[1]==tab[4]==tab[7]) or(tab[0]==tab[4]==tab[8]) or(tab[2]==tab[4]==tab[6]):
        return True
    else:
        return False
        
startScreen()
while (liczbaRuchów < 9):
    os.system('clear')
    circleMove()
    if (win()==True):
        print(name1,"wygrywa!")
        break
    liczbaRuchów += 1
    if (liczbaRuchów == 9):
        print ("Gra zakończona remisem!")
        break
    os.system('clear')
    crossMove()
    if (win()==True):
        print(name2,"wygrywa!")
        break
    liczbaRuchów += 1
    print(tab)