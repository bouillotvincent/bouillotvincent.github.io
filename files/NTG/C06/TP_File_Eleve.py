def file():	
    """ crée une file vide """ 	
    return []	
	
def est_vide(f):	
    """renvoie True si la file est vide	
     et False sinon"""	
    return f == []	
	
def enfiler(f, x):	
    """Ajoute l’élément x à la file f"""	
    f.append(x)	
	
def defiler(f):	
    """enlève et renvoie le premier élément de la file f""" 	
    assert not est_vide(f), "File vide"	
    return f.pop(0)	

import random



class File:	
    """ classe File : 	
    création d’une instance File avec à partir d'une liste """	
    def __init__(self):	
        """Initialisation d’une file vide"""	
		
		
    def est_vide(self):	
        """teste si la file est vide""" 	
        return	
		
    def defiler(self): 	
        """défile"""	
       	
        return	
		
    def enfiler(self, x): 	
        """enfile"""