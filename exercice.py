#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import turtle


# TODO: Définissez vos fonction ici
def masse_elipse(axe_A=1, axe_B=1, axe_C=1, masse_volumique=1):
    volume = 4/3*pi*axe_A*axe_B*axe_C
    masse = masse_volumique*volume

    return (volume, masse)

def frequence(sentence: str) -> dict:
    lettres_repetees={}
    lettres_repetees5={}
    for lettre in sentence:
        lettres_repetees[lettre]=0
    for lettre in sentence:
        lettres_repetees[lettre]+=1
    for lettre in lettres_repetees:
        if lettres_repetees[lettre]<=5:
            lettres_repetees5[lettre]=lettres_repetees[lettre]
    return lettres_repetees5

def frequenceElevee(sentence):
   return sorted(frequence(sentence)).items(), key = lambda item: item[1], reverse = True)[0]

def arbre(niveau=0, longueur_branche=0, angle=0):
    coef=2/3
    if niveau == 0:
        return
    
    turtle.down()
    turtle.forward(longueur_branche)
    turtle.left(angle)

    arbre(niveau-1, longueur_branche*coef, angle)
    turtle.right(2*angle)

    arbre(niveau-1, longueur_branche*coef, angle)
    turtle.left(angle)

    turtle.backward(longueur_branche)

def get_sequence(prompt):
    while True:
        chaine = input(f'{prompt}:')
        if valider_adn(chaine):
            break
        else:
            print(f'{prompt} invalide')
    return chaine


def valider_adn(adn: str) -> bool:
    if len(adn) != 0:
        for lettre in adn:
            if lettre not in ['a','t','g','c']:
                return False
        return True    
    return False



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(masse_elipse())
    arbre()
    get_sequence()
    print(frequenceElevee)


    pass
