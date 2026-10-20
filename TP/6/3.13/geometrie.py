from math import pi

def aire_rectangle(longueur: float, largeur: float)-> float:
    return largeur * largeur

def aire_carre(cote: float)-> float:
    return cote ** 2

def aire_triangle(base: float, hauteur: float)-> float:
    return (base * hauteur) /2

def aire_cercle(rayon: float)-> float:
    return pi * rayon**2
