import random

class Personnage:
    probaCC = 0.5
    print(probaCC)

    def __init__(self, nom, pointsDeVie, pointsDeForce):
        """ constructeur de la classe """
        self.vie = pointsDeVie
        self.force = pointsDeForce
        self.nom = nom

    def donneEtat(self):
        """ renvoie les points de vie de mon personnage """
        return self.vie

    # def estBlessePar2(self, valeur):
    #     print(self.probaCC)
    #     if random.random() > self.probaCC:
    #         self.vie -= valeur*2
    #         print('Coup Critique!')
    #     else :
    #         self.vie -= valeur
    #     print(f'{self.nom} a {self.vie} points de vie restants.')
    
    def estBlessePar(self, ennemi):
        """ 
        self perd le nombre de points de force de l'ennemi 
        Attention, else évite que self s'attaque lui-même !
        """
        if self.nom != ennemi.nom:
            self.vie = self.vie - self.critique(ennemi.force)
            print(f'{ennemi.nom} frappe {self.nom}. {self.nom} a {self.vie} points de vie restants')
        else:
            print('On ne se suicide pas en Terre du milieu')

    def critique(self, valeur):
        """
        calcule si un coup est critique ou non
        """
        if random.random() > self.probaCC:
            print('Coup Critique!')
            return valeur*2
        else :
            return valeur
    

def game():
    sauron = Personnage('Sauron', 20, 5)
    isildur = Personnage('Isildur', 40, 3)
    while isildur.donneEtat()>0 and sauron.donneEtat()>0 :
        # Sauron attaque toujours en premier car Isildur 
        # était en train de ramasser des chanterelles...
        if sauron.donneEtat()>0: isildur.estBlessePar(sauron)
        if isildur.donneEtat()>0: sauron.estBlessePar(isildur)
    if sauron.donneEtat()<=0 and isildur.donneEtat()>0:
        msg = f"Isildur est vainqueur, il lui reste encore {isildur.donneEtat()} points alors que Sauron est mort"
    elif sauron.donneEtat()>0 and isildur.donneEtat()<=0:
        msg = f"Sauron est vainqueur, il lui reste encore {sauron.donneEtat()} points alors que Isildur est mort"
    else :
        msg = "Les deux combattants sont morts en même temps"
    return msg

print(game())


""" Tests de fin de programme """
# isildur.donneEtat()
# sauron.donneEtat()
# isildur.estBlessePar()
# isildur.donneEtat()
# sauron.estBlessePar()
# sauron.donneEtat()

# sauron.estBlessePar(isildur)
# isildur.estBlessePar(sauron)
# sauron.estBlessePar(isildur)

# print(isildur.vie)

# print(sauron.vie)

# sauron = Personnage('Sauron', 20, 5)
# isildur = Personnage('Isildur', 40, 3)

# print(sauron.donneEtat())
# #sauron.estBlessePar(isildur.donneEtat()[1])
# print(sauron.donneEtat())
