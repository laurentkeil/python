#/usr/bin/env python
# -*- coding: utf-8 -*-

def pair (nb):
    if (nb % 2 == 0):
        return "noir"
    else :
        return "rouge"

from random import randrange

sommeTotal = 100
continuerGame = True

while(continuerGame) :

    print("Vous avez une somme de ", sommeTotal, " $")
    
    nbrChoisi = -1
    while (nbrChoisi < 1 or nbrChoisi > 50):
        nbrChoisi = input("Choisir un nombre entre 1 et 50 : ")
        try : 
            nbrChoisi = int(nbrChoisi)
        except ValueError:
            print("Ce n'est pas un nombre.")
        if(nbrChoisi < 1 or nbrChoisi > 50):
            print("Nombre incorrect")

    couleurNbChoisi = pair(nbrChoisi)
    
    mise = 0
    while (mise <= 0 or mise > sommeTotal) :
           mise = input("Choisir une mise ($) : ")
           # On convertit la mise
           try:
               mise = int(mise)
           except ValueError:
               print("Vous n'avez pas saisi de nombre")
               mise = -1
               continue
           if mise <= 0:
               print("La mise saisie est négative ou nulle.")
           if mise > sommeTotal:
               print("Vous ne pouvez pas miser autant, vous n'avez que", sommeTotal, "$")

    nbrAleatoire = randrange(50) ++ 1
    couleurNbAl = pair(nbrAleatoire) 
    print("Tirage du nombre ", nbrAleatoire, " de couleur ", couleurNbAl)

    if (nbrChoisi == nbrAleatoire) :
        print("Vous avez gagné !")
        sommeTotal += 3*mise
    elif (couleurNbChoisi == couleurNbAl) :
        print("La couleur est la même")
        sommeTotal -= mise/2
    else : 
        print("Vous avez perdu !")
        sommeTotal -= mise

    if(sommeTotal <= 0) :
        print("Vous n'avez plus rien, au revoir !")
        continuerGame = False
    else :
        print("Vous avez encore ", sommeTotal, " $")
        continuer = "Y"
        continuer = input("Continuer (Y/N) ?")
        continuerGame = continuer == "Y" or continuer == "y"