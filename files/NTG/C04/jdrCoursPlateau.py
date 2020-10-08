import random
import os

class Personnage:
    probaCC = 0.5

    def __init__(self, nom, pointsDeVie, pointsDeForce, position):
        """ initialise les attributs initiaux (en particulier position) """
        self.vie = pointsDeVie
        self.force = pointsDeForce
        self.nom = nom
        self.position = position
    
    def donneEtat(self):
        """ renvoie les points de vie """
        return self.vie

    def estBlessePar2(self, valeur):
        """ fonction obsolète """
        if random.random() > self.probaCC:
            self.vie -= valeur*2
            print('Coup Critique!')
        else :
            self.vie -= valeur
        print(f'{self.nom} a {self.vie} points de vie restants.')
    
    def estBlessePar(self, personnage):
        """ mutateur : perso1.estBlessePar(ennemi) """
        if self.nom != personnage.nom:
            self.vie = self.vie - self.critique(personnage.force)
            print(f'{personnage.nom} frappe {self.nom}. {self.nom} a {self.vie} points de vie restants')
        else:
            print('On ne se suicide pas en Terre du milieu')

    def critique(self, valeur):
        """ gestion des coups critiques """
        if random.random() > self.probaCC:
            print('Coup Critique!')
            return valeur*2
        else :
            return valeur
        
    def setPosition(self, valeur):
        """ mutateur *pur* de la position """
        self._position = valeur
        
    def getPosition(self):
        """ accesseur *pur* de la position """
        return self._position

    def peutAttaquer(self, personnage):
        """ indique si mon personnage peut attaquer ou non """
        if self.distance(self.position, personnage.position) == 1:
            return True
        return False

    def distance(self, ptA, ptB):
        """ calcul la distance de Manhattan entre deux points :
            +XXX+
            +XoX+
            +XXX+
            +++++
        """
        # distance de Manhattan
        deltaX = abs(ptA[0]-ptB[0])
        deltaY = abs(ptA[1]-ptB[1])
        return max(deltaX, deltaY)

    """ property permet de mimer des attributs privées de classe """
    position = property(fset=setPosition, fget=getPosition)


class Plateau:
        
    """ def afficheGrille(self): affiche la grille ligne par ligne """
    """def majGrille(self, *personnage): met à jour la grille en fonction des
    positions des personnages """
    def __init__(self, taille):
        """ initialise 
        - taille : entier
        - plateau : sous forme de tableau de tableau 
        """
        self.taille = taille
        self.grille = [['_']*self.taille for i in range(self.taille)]
    
    def __len__(self):
        """ renvoie la taille du plateau lors d'un appel à len(Grille)"""
        return self.taille
    
    def afficheGrille(self):
        """ affiche la grille ligne par ligne """
        for lignes in self.grille:
            print(lignes)
        print()

    def majGrille(self, *personnage):
        """ mise à jour du plateau de jeu :
        on recrée une grille vierge et on replace tous les personnages grâce à une boucle
        le *personnage permet de passer un nombre variable de personnages à la méthode majGrille
        """
        os.system('clear')
        self.grille = [['_']*self.taille for i in range(self.taille)]
        for perso in personnage:
            X, Y = perso.getPosition()
            self.grille[X][Y] = perso.nom[0]   # Initiales du personnage
        self.afficheGrille()

    """ def __init__(self):  initialise le nombre de coup """
    # def deplacement(self): """ gère les déplacements : utilisez un dictionnaire! """
    #    dico = {'Z': [-1, 0] , 'S': [1, 0], 'Q': [0, -1], 'D': [0, 1]}
    """ def finJeu(self, *personnage): le jeu est-il fini ? """
    """ def choix(self) : choix pour attaquer un perso """
    """ def run(self, Grille, *personnage): lance le jeu ! """
    """ def setTicks(self): compte les tours de jeu """    
    """ def getTicks(self): renvoie les tours de jeu  """

class Game:

    def __init__(self):
        """ initialise le nombre de tours à 0 """
        self.ticks = 0

    def deplacement(self):
        """ règles de déplacement. On utilise un dictionnaire pour simplifier les choses:
            Exemple :
            dico['Z'] va renvoyer [-1,0] que l'on doit ajouter à la position des personnages
        """
        dico = {'Z': [-1, 0] , 'S': [1, 0], 'Q': [0, -1], 'D': [0, 1]}
        a = True
        while a:
            try : # le joueur entre une valeur au clavier : on essaie d'accéder à dico[key]
                key = input(str([f'{i}' for i in dico.keys()])+' ').capitalize()
                return dico[key] 
            except KeyError : # si key ne fait pas partie de dico, on recommence!
                a = True

    def continueJeu(self, *personnage):
        """ regarde l'état de tous les personnages. Si un personage a un état < 0, boolean devient False
        Cela termine le jeu.
        """
        boolean = True
        for perso in personnage:
            if perso.donneEtat()>0 and boolean:
                boolean = True
            else : boolean = False
        return boolean

    def choix(self, ennemi):
        """ gestion des attaques : le joueur peut choisir de s'enfuir plutôt que d'attaquer """
        key = input(f'Voulez-vous attaquer {ennemi.nom}? Votre tour sera terminé. O ? ').capitalize()
        return True if key == 'O' else False
        

    def run(self, Grille, *personnage):
        """ la méthode pour jouer ! et c'est un poil le bazar...
        Important : avec l'opérateur % len(Grille), les personnages qui "sortent" du plateau
        traversent et vont de l'autre coté (voir classe Fraction)
        """
        boolean = True
        Grille.majGrille(*personnage)
        while boolean: # tant que personne n'est mort, on continue.
            for perso in personnage: # chaque personnage doit pouvoir jouer
                print(f'⚔️ ⚔️ ⚔️ ⚔️   Tour de {perso.nom} ⚔️ ⚔️ ⚔️ ⚔️')
                for opponent in personnage: 
                    if perso != opponent:
                        choix = False
                        #print(perso.nom, opponent.nom, perso.peutAttaquer(opponent))
                        if perso.peutAttaquer(opponent):
                            choix = self.choix(opponent)
                        if choix:
                            print(f'{perso.nom} a attaqué!')
                            opponent.estBlessePar(perso)
                            boolean = self.continueJeu(*personnage)
                print(choix)
                if not choix:
                    # deplacement si on attaque pas.
                    move = self.deplacement()
                    nouvellePos = [(perso.position[0] + move[0]) % len(Grille), \
                                   (perso.position[1] + move[1]) % len(Grille)]
                    for opponent in personnage:
                        while [nouvellePos[0], nouvellePos[1]] == opponent.position:
                            print('Vous ne pouvez pas marcher sur votre ennemi!')
                            move = self.deplacement()
                            nouvellePos[0] = (perso.position[0] + move[0]) % len(Grille)
                            nouvellePos[1] = (perso.position[1] + move[1]) % len(Grille)
                    perso.position = nouvellePos  # mise à jour de la position de mon personnage
                    print(f'{perso.nom} a bougé!')
                    Grille.majGrille(*personnage)

            boolean = self.continueJeu(*personnage)

    def setTicks(self):
        self.ticks += 1
    
    def getTicks(self):
        return self.ticks
    
    #tk.mainloop() 


# Initialisation avec position aléatoire
grid = Plateau(5)
sauron = Personnage('Sauron', 20, 5, [random.randint(0,len(grid)-1),random.randint(0,len(grid)-1)])
isildur = Personnage('Isildur', 40, 3, [random.randint(0,len(grid)-1),random.randint(0,len(grid)-1)])
elrond = Personnage('Elrond', 20, 4, [random.randint(0,len(grid)-1),random.randint(0,len(grid)-1)])

# Lancement du jeu !
Game().run(grid, sauron, isildur, elrond)