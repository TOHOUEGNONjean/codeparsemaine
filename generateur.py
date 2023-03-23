#coding: utf-8
#on importe le module sys de python 
from sys import *
'''
    definition de la fonction generateur

'''

def generateur():
    for i in range(106): 
        yield i
#on recupère les informations de la fonction generateur dans une variable "mavar"
mavar = generateur()

#essayons d'afficher la liste créer par notre fonction generateur
for i in mavar:
    print(i)

'''
    en utilisant la fonction getsizeof, visualisons l'espace memoir utiliser par cette variable 
'''
print('En utilisant un générateur la taille est : {} '.format(getsizeof(mavar)))

#création de la liste en compréhension

tab = [i for i in range(106)]
#affichons le tableau
print(tab)

'''
    Meme chose pour la variable tab
'''
print('En utilisant une comphréhension de liste, la mémoire est : {} '.format(getsizeof(tab)))

conclusion1 = "1- Remarquons que les deux méthodes affiches les mêmes listes comme resultat "
conclusion2 = "2- Les deux méthodes utilisent d'une façon différente la mémoire"
conclusion3 = "3- les genarateurs ne peuvent passer qu'un seul élément en memoire mais les listes stockent tout les éléments "

print(" {} \n {} \n {}" . format(conclusion1, conclusion2, conclusion3))