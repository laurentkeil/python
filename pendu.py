#/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ce fichier contient le jeu du pendu.
Il s'appuie sur les fichiers :
- datas.py
- functions.py"""


from datas import *
from functions import *

# On récupère les scores de la partie
scores = scoresRecup()
# On récupère un nom d'utilisateur
user = nameUserRecup()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if user not in scores.keys():
	scores[user] = 0 # 0 point pour commencer

# Notre variable pour savoir quand arrêter la partie
continue_game = 'y'

while (continue_game != 'n') :

	print("\nBienvenue dans le jeu du pendu, joueur {0}, vous avez {1} points.".format(user, scores[user]))
	mot_choisi = wordChoice()
	lettres_trouvees = []
	mot_mystere = wordRecup (mot_choisi, lettres_trouvees)
	nb_chances = nb_coups

	while (nb_chances > 0 and mot_mystere != mot_choisi) :

		print("Trouver le mot : {0}. Il vous reste {1} coups à jouer".format(mot_mystere, nb_chances))
		lettre = lettreRecup()
		if (lettre in mot_choisi and lettre not in lettres_trouvees) :
			print("Bien joué.")
			lettres_trouvees.append(lettre)
		elif (lettre in mot_choisi) :
			print("Lettre déjà trouvée.")
		else :
			print("Bad.")
			nb_chances -= 1
		mot_mystere = wordRecup (mot_choisi, lettres_trouvees)

	if (mot_mystere == mot_choisi) :
		print("Félicitations ! Vous avez trouvé le mot {0} avec {1} point(s).".format(mot_mystere, nb_chances))
	else :
		print("PENDU !!! Vous avez perdu.")

	scores[user] += nb_chances
	continue_game = raw_input("Voulez-vous continuer la partie (y/n) ?")
	continue_game = continue_game.lower()
	print(continue_game)


# La partie est finie, on enregistre les scores
scoresSave(scores)

# On affiche les scores de l'utilisateur
print("Vous finissez la partie avec {0} points.".format(scores[user]))