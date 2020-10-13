import tkinter as tk

class dessinePile :
    """ Cette classe représente l'état de la pile à l'aide de schémas réalisés avec Tkinter.
        Instructions à placer où vous le souhaitez dans votre programme :
            1) Initialisation de Tkinter: root = tk.Tk()
            2) Création du graphique: a = dessinePile(root)
            3) Inspection de la pile: a.ajoutePile(inspect.stack())
            4) Affichage fenêtre graphique: root.mainloop()
        dessinePile prend deux arguments optionnels width et height gérant la taille de la fenêtre graphique.
    """

    def __init__(self, master, width = 800, height = 400):
        self.fen = master
        self.fen.title("Pile d'exécution")

        self.padding = 20
        self.size = [100, 50]
        self.largeur, self.hauteur = self.size
        
        self.dessin = tk.Canvas(self.fen, width = width, height = height, bg = 'white')
        self.dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)
        self.fen.update() # to update winfo_width

    def _dessine(self, text):
        """ Positionne le rectangle et le contenu dans la fenêtre Tkinter.
            Cette méthode est privée et ne doit pas être appelée par un utilisateur.
        """
        fenH = self.dessin.winfo_height()
        y0, y1 = fenH - self.hauteur - 10, fenH - (self.hauteur-50) - 10
        x0, x1 = self.padding + (self.largeur-self.size[0]), self.padding + self.largeur
        self.dessin.create_rectangle(x0, y0, x1, y1)
        self.dessin.create_text((x0+x1)/2, (y0+y1)/2, text=text, justify=tk.CENTER)

    def ajoutePile(self, frameInfoList):
        """ Dessine une pile à partir d'une liste de frame obtenu à l'aide du module inspect.
            Pour ajouter une pile, frameInfoList doit prendre pour valeur inspect.stack()
        """        
        for frame in frameInfoList[::-1]:
            textFull = str(frame[0])
            text = (textFull[textFull.index('code'):textFull.index('>')]+ '\n' 
                   +textFull[textFull.index('at')+3:textFull.index(',')]+ '\n' 
                   +textFull[textFull.index('line'):textFull.index(',',textFull.index('line'))])
            self._dessine(text)
            self.hauteur += self.size[1]
        self.largeur += self.size[0] +self.padding
        self.hauteur = self.size[1]