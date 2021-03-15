import requests
from GViz import *

def strip(DICO):
    """ fonction utile pour le cas réel"""
    return [mot.split('/')[0] for mot in DICO]

def dictionnaireDL(url):
    """
    Récupère une liste de mot depuis un dépot GitHub
    Renvoie une liste de mots d'une langue donnée
    """
    download = requests.get(url)
    DICO = download.content.decode('utf-8').split('\n')
    DICO = strip(DICO)
    
    #affichage ligne par ligne du dictionnaire
    for ligne in DICO :
        print(ligne)

    return DICO

url = "https://github.com/bouillotvincent/coursNSI/blob/master/dico110.dic"
# récupère une liste 
d110 = dictionnaireDL(url)  

def distance(mot1, mot2):
    if len(mot1) != len(mot2):
        return -1
    dist = 0
    nLettres = len(mot1) 

    pass

print(distance('montre', 'mentor'))

def genGraphe(dictionnaire):
    """
    Paramètres d'entrée : un dictionnaire de la langue française sous forme de tableau de mots
    Sortie : un graphe de la classe GrapheDico
    """

    pass

#Application(genGraphe(d110), width=1000,height=750).mainloop()