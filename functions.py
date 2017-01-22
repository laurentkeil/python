#/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ce fichier définit des fonctions utiles pour le programme pendu.

On utilise les données du programme contenues dans donnees.py"""

import os
import pickle
from random import choice

from datas import *

#gestion scores

def scoresSave (scores) :
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores
    à enregistrer"""
    
    scores_file = open(nom_fichier_scores, "wb")
    mon_pickler = pickle.Pickler (scores_file)
    mon_pickler.dump (scores)
    scores_file.close()
    
def scoresRecup () :
    """Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire, 
        soit l'objet dépicklé,
        soit un dictionnaire vide.
    On s'appuie sur nom_fichier_scores défini dans donnees.py"""

    if os.path.exists(nom_fichier_scores) : # Le fichier existe
        # On le récupère
        scores_file = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler (scores_file)
        scores = mon_depickler.load ()
        scores_file.close()
    else : scores = {}
    return scores
    
#gestion de saisie du user    

def nameUserRecup () :
    """Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.
    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau"""

    name_user = raw_input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    name_user = name_user.capitalize()
    if (not name_user.isalnum() or len(name_user) < 4) :
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return nameUserRecup()
    else:
        return name_user
        
def lettreRecup() :
    """Cette fonction récupère une lettre saisie par
    l'utilisateur. Si la chaîne récupérée n'est pas une lettre,
    on appelle récursivement la fonction jusqu'à obtenir une lettre"""

    lettre = raw_input("Tapez une lettre: ")
    lettre = lettre.lower()
    if (len(lettre) > 1 or not lettre.isalpha()) :
        print("Vous n'avez pas saisi une lettre valide.")
        return lettreRecup()
    else :
        return lettre

#gestion du pendu

def wordChoice() :
    """Cette fonction renvoie le mot choisi dans la liste des mots
    liste_mots.
    On utilise la fonction choice du module random (voir l'aide)."""
    
    return choice(liste_mots)

def wordRecup(mot_complet, lettres_trouvees) :
    """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)
    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées."""
    word_to_found = ""
    for lettre in mot_complet :
        if lettre in lettres_trouvees :
            word_to_found += lettre
        else :
            word_to_found += "*"
    return word_to_found