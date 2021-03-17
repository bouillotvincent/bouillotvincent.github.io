from tkinter import *
from random import *
from math import sqrt, pi, cos, sin, atan2
from itertools import groupby
import time

class Noeud:
    
    def __init__(self, g = None, v=0, d=None):
        self.gauche = g
        self.valeur = v
        self.droit = d


class Application(Tk):

    _color = 255

    def __init__(self, G, weight = False, arrow = True, width = 500, height = 500):
        Tk.__init__(self)        # constructeur de la classe parente
        self.can = Canvas(self, width = width, height = height, bg ="white")
        self.can.grid(row = 0, rowspan = 78, column = 0)
        self.can.update()
        self.a = {}
        self.params = G
        self.ell = []
        self.weight = weight
        self.flag = False
        # if G is a Node (ie binary tree), don't show arrows
        if not isinstance(G, Noeud): self.arrow = arrow
        else: self.arrow = False
        self.move = ''
        self.connect = []
        self.dessine(G, self.generateRegular)
        self.can.bind('<Button-1>', self.startMove)
        self.can.bind('<Motion>', self.hover)
        self.can.bind('<ButtonRelease-1>', self.stopMove)
        # self.can.bind('<Button-3>', self.startConnect)
        # self.can.bind('<ButtonRelease-3>', self.stopConnect)
        Button(self, text = "Polygone Regulier", command = lambda x=3: self.dessine(G,self.generateRegular)).grid(row = 1, column = 1)
        Button(self, text = "Grille", command = lambda x=3: self.dessine(G,self.generateGrid)).grid(row = 2, column = 1)
        Button(self, text = "Parcours préfixe", command = lambda x=3: self.drawParcours(self.params[0], 'préfixe')).grid(row = 3, column = 1)
        Button(self, text = "Parcours infixe", command = lambda x=3: self.drawParcours(self.params[0], 'infixe')).grid(row = 4, column = 1)
        Button(self, text = "Parcours suffixe", command = lambda x=3: self.drawParcours(self.params[0], 'suffixe')).grid(row = 5, column = 1)
        #Button(self, text = "Parcours largeur", command = lambda x=3: self.drawParcours(self.params[0], 'largeur')).grid(row = 5, column = 1)
        Button(self, text = "Coloration : Glouton Simple", command = lambda x=3: self.colorier('G1')).grid(row = 7, column = 1)
        Button(self, text = "Coloration : Glouton", command = lambda x=3: self.colorier('G1+')).grid(row = 8, column = 1)
        Button(self, text = "Coloration : DSATUR", command = lambda x=3: self.colorier('DSATUR')).grid(row = 9, column = 1)
        okCmd = self.can.register(self.callback)
        self.sv = StringVar()
        self.ent = Entry(self, textvariable = self.sv, validate = "all", validatecommand = (okCmd, '%P'))
        self.ent.grid(row = 80, column = 0, columnspan = 2, sticky='EW', padx = 20)
        # self.lab = Label(self, text = '')
        # self.lab.grid(row = 4, column = 5)

    def callback(self, value):
        #self.ent.configure(text = self.sv + 'z')
        if validerArbre(value):
            self.params[0] = construireArbre(value)
            if self.params[0] is not None:
                self.a = {}
                self.dessine(self.params[0], eval('self.' + self.params[1]))
            return True
        else: return True

    #def startDraw(self):
    #    self.params[0] = construireArbre("[[None]A[None]]")
    #    self.dessine(self.params[0], eval('self.'+self.params[1]))

    def startMove(self, event):
        """ Démarre le déplacement d'un noeud """
        self.getCircle(event.x, event.y)
        #self.a[str(self.move)].cerclePeint(color = 'red')

    def hover(self, event):
        """ Déplacement du noeud """
        if len(self.move) != 0:
            self.moveTo(event.x, event.y)

    def stopMove(self, event):
        """ Arrête le déplacement du noeud 
        Aucun update de la fenêtre graphique
        """
        self.move = ''

    def getCircle(self, x, y, r = 15):
        """ Détecte le noeud à déplacer """
        for text in self.a.keys():
            X = self.a[text].x
            Y = self.a[text].y
            if (x-X)**2+(y-Y)**2 <= r**2 and "none" not in text:
                self.move = text


    def parcours(self):
        pass
    # def startConnect(self, event):
    #     """ Démarre le déplacement d'un noeud """
    #     self.getCircle2(event.x, event.y)

    # def stopConnect(self, event):
    #     """ Arrête le déplacement du noeud """
    #     self.connect = []                

    # def getCircle2(self, x, y, r = 15):
    #     """ Détecte le noeud à déplacer """
    #     for text in self.a.keys():
    #         X = self.a[text].x
    #         Y = self.a[text].y
    #         if (x-X)**2+(y-Y)**2 <= r**2 and "none" not in text:
    #             self.connect.append(text)

    def moveTo(self, x, y, r = 15):
        """ 
        Nouvelles coordonnées pour le noeud déplacé
        Mise à jour de la fenêtre graphique
        """
        self.a[self.move].x = x
        self.a[self.move].y = y
        G = self.params
        self.dessine(G, self.generateRegular)

    def taille(self, G: Noeud):
        if G is None : return 0
        else : 
            return 1 + self.taille(G.gauche) + self.taille(G.droit)

    def hauteur(self, G: Noeud):
        if G is None : return 0
        else : 
            return 1 + max(self.hauteur(G.gauche), self.hauteur(G.droit))
    
    def listeFils(self, noeud, dico):
        base = dico[noeud]
        fils = []
        for key, value in dico.items():
            if value == base + '0' or value == base + '1':
                fils.append(key)
        return fils       

    def _getEllipseParameter(self, text):
        a = self.can.create_text(0, 0, text = text)
        bounds = self.can.bbox(a)  # returns a tuple like (x1, y1, x2, y2)
        self.can.delete(a)
        a, b  = bounds[2] - bounds[0], bounds[3] - bounds[1]
        return a, b

    def dessine(self, G, func):
        self.can.delete('all')
        #print('tp', G, isinstance(G, Noeud), )#len(G.listeSommets()))
        if not isinstance(G, Noeud) : # Graph entered as a dictionnary
            print('367', self.move, len(self.move), not len(self.move))
            if not len(self.move):  
                # First generation of coordinates following the rules defined by func
                listCoords = func(len(G.listeSommets()))
                #Create GraphViz objects
                for i,text in enumerate(G.listeSommets()):
                    r1, r2 = self._getEllipseParameter(text)
                    self.a[text] = graphViz(self.can, listCoords[i][0], listCoords[i][1], text, self.arrow, a=r1, b=r2)
            else:
                # Redefinition of coordinates following a click-and-drag
                listCoords = [(self.a[text].x, self.a[text].y) for text in self.a]
                # Alter graphViz objects
                for i, text in enumerate(self.a) :
                    self.a[text].x, self.a[text].y = listCoords[i][0], listCoords[i][1]

            if self.weight: local = []
            for text in G.listeSommets():
                self.a[text].cercles(self.can,self.a[text].x,self.a[text].y)
                for sommet in G.listeVoisins(text):
                    r1, r2 = self._getEllipseParameter(sommet)
                    if G.isDoubleArc(text, sommet) and self.arrow: 
                        self.flag = not self.flag
                        self.a[text].line(self.can,self.a[text].x,self.a[text].y, \
                            self.a[sommet].x, self.a[sommet].y, r1target = r1, r2target= r2,  flag = self.flag)
                    else: 
                        self.a[text].line(self.can,self.a[text].x,self.a[text].y, \
                            self.a[sommet].x,self.a[sommet].y, r1target = r1, r2target= r2)

                    if self.weight:
                        #print('ligne 273', text, sommet, G.listeVoisins(text)[sommet])
                        local.append((text, sommet))
                        if (sommet, text) not in local:
                            #print('ligne 276', text, sommet, G.listeVoisins(text)[sommet])
                            self.a[text].weightText(self.can,self.a[text].x,self.a[text].y, self.a[sommet].x,self.a[sommet].y,G.listeVoisins(text)[sommet])    

        else: # Binary tree entered as Nodes
            #dico = {}
            dico = self.parcoursInfixe(G, '', {})
            if not len(self.move):
                # First generation of coordinates following the rules defined by func
                listCoords = self.generateTree(self.hauteur(G))[::-1]
                listIndex = [self._bin2index(dico[i]) for i in self.parcoursLargeur(G)]
                coords = [listCoords[i] for i in listIndex]
            else:
                # Redefinition of coordinates following a click-and-drag
                coords = [(self.a[text].x, self.a[text].y) for text in self.a]

            dico = self.triage(dico)
            print(dico)
            for i, text in enumerate(dico.keys()):
                self.a[text] = graphViz(self.can, coords[i][0], coords[i][1], text, self.arrow)

            for text in dico.keys():
                if('None' not in text.capitalize() if isinstance(text, str) else text): 
                    self.a[text].cercles(self.can,self.a[text].x,self.a[text].y)
                for sommet in self.listeFils(text, dico):
                    self.a[text].line(self.can,self.a[text].x,self.a[text].y, self.a[sommet].x,self.a[sommet].y)


    def triage(self, dico):
        """ 
        Create a sorted (ordered) dict. 
        Sorting is done along the length of the values of the keys
        '' will be top node of tree
        '0', '1' will be second level
        '00', '01', '10', '11' will be third level...
        {'a': '', 'c': '0', 'b': '1', 'k': '10', 'f': '11'}
        """
        sortedValues = sorted(dico.values(), key=lambda x:len(x))
        return { key:value for val1 in sortedValues for key, value in dico.items() if value == val1 }
    

    def parcoursLargeur(self, G: Noeud):
        f = [G]
        tNodes = []
        while len(f) != 0:
            x = f.pop(0)
            if x.gauche != None:
                Tg = x.gauche
                f.append(Tg)
            if x.droit != None:
                Td = x.droit
                f.append(Td)
            tNodes.append(x.valeur)            
        return tNodes

    def generateTree(self, hauteur):
        """ 
        Generate the coordinates (x,y) of the leaves for a perfect binary tree
        Adapts to the current window size
        """
        w = self.can.winfo_width()
        h = self.can.winfo_height()
        nTerminalLeaves = max(2**(hauteur-1), 2)
        # il y a un "trou" en moins qu'une feuille 
        absXLeaves = [i*(w-50)/(nTerminalLeaves-1)+25 for i in range(nTerminalLeaves-1,-1,-1)]
        a = [[i*(w-50)/(nTerminalLeaves-1)+25 for i in range(nTerminalLeaves-1,-1,-1)]]
        self.posTree(absXLeaves, a)
        return [(a[hauteur-j-1][i], h/hauteur*j+20) for j in range(hauteur-1,-1,-1) for i in range(len(a[hauteur-j-1]))]

    def posTree(self, absX, u):
        """ 
        X-coordinates of leaves in tree.
        Start from terminal leaves
        """
        if len(absX) == 2: 
            u.append([(absX[0]+absX[1])/2])
            return (absX[0]+absX[1])/2
        else : 
            u.append([(absX[i]+absX[i+1])/2 for i in range(0,int(len(absX)),2)])
            return self.posTree([(absX[i]+absX[i+1])/2 for i in range(0,int(len(absX)),2)], u)

    def generateRegular(self, n):
        w = self.can.winfo_width()
        h = self.can.winfo_height()        
        return [(w/2 + w/3 * cos(i*2*pi/n),  h/2 + h/3 * sin(i*2*pi/n)) for i in range(n)]


    def generateGrid(self, n):
        w = self.can.winfo_width()
        h = self.can.winfo_height()
        nCol = int(sqrt(n))
        nLigne = 0
        while nCol * nLigne < n:
            nLigne += 1
        return [(i* w / nCol % w + w / (2*nCol),  j*h / nLigne % h+h / (2*nLigne)) for i in range(nCol) for j in range(nLigne)]


    def parcoursInfixe(self, a, txt, dico):
        if a is None: return
        self.parcoursInfixe(a.gauche, txt+'0', dico)
        while a.valeur in dico: 
            a.valeur += '.'
        dico[a.valeur] = txt
        self.parcoursInfixe(a.droit, txt+'1', dico)
        return dico
 
    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   

    def drawParcours(self, arbre, type = "infixe", call = 1):        
        if call == 1 : 
            self.clearColor()
        if arbre is None: return
        if type == "préfixe":self._animatePaint(arbre)
        self.drawParcours(arbre.gauche, type, 2)
        if type == "infixe": self._animatePaint(arbre)
        self.drawParcours(arbre.droit, type, 2)
        if type == "suffixe": self._animatePaint(arbre)

    # def drawParcoursG(self, graphe, type = "infixe", call = 1): 
    #     if call == 1 : 
    #         self.clearColor()
    #     graphe.couleur[source] = 'NOIR'
    #     for v in graphe.listeVoisins(source):
    #         self._animatePaint(graphe)
    #         if graphe.couleur[v] != 'NOIR':
    #             self.drawParcoursG(graphe)

    def colorier(self, key, call = 1 ):        
        self.clearColor()
        try :
            if key == 'DSATUR' : couleur = colorationDSATUR(self.params)
            elif key == 'G1': couleur = colorationG1(self.params)
            elif key == 'G1+': couleur = colorationG1p(self.params)
        except :
            raise Exception("Votre méthode n'est pas programmée")
        colnames = ['red', 'green', 'blue', 'yellow', 'orange', 'magenta', 'grey', 'cyan', 'teal']
        for i in self.a:
#            col = int(self._color / (couleur[i]+1))
            self.a[i].cerclePeint(color = colnames[couleur[i]])
        self.can.update()
        
    def clearColor(self):
        """ to maintain """
        for i in self.a:
            print(i)
            self.a[i].cerclePeint(color = self._from_rgb((255, 255, 255)))
        self.can.update()

    def _animatePaint(self, arbre, pause = 1):
        n = len(self.a)
        self.a[arbre.valeur].cerclePeint(color = self._from_rgb((0, self._color, 0)))
        self._color -= int(self._color / n) # change update based on number of nodes
        self.can.update()
        time.sleep(pause)

    def _bin2index(self, txt):
        """ 
        genère les indices dans le tableau permettant de représenter l'arbre
        a level n has 2**n-1 parent nodes overall 
        """
        n = len(txt)
        start = 2**n-1
        if txt == '' : return 0
        return start + int(txt, base=2)

    # def cerclePeint(self, node, color = 'white'):
    #     if node != '':
    #         self.can.itemconfig(self.a[node].cercleID, fill = color)
    #         self.a[node].color = color




class graphViz:
    """ 
    class graphViz
    handles the drawing of lines between, circles of and text on nodes of a graph 
    (or a binary tree).
    """
    def __init__(self, canev, x, y, text, arrow, color = 'white', rayon = 15, a = 0, b = 0):
        self.canev, self.x, self.y, self.arrow = canev, x, y, arrow
        self.a, self.b  = a, b
        self.text = text
        self.r = rayon
        self.cercleID = 0
        self.color = color

    def cercles(self, canev, x, y):
        # a = self.canev.create_text(x, y, text=self.text)
        # bounds = self.canev.bbox(a)  # returns a tuple like (x1, y1, x2, y2)
        # self.canev.delete(a)
        # a, b  = bounds[2] - bounds[0], bounds[3] - bounds[1]
        self._cercleAdaptive(canev, x, y, self.a, self.b)
        self.canev.create_text(x, y, text=self.text)
#        print('PIF', self.canev.coords(a), width, height)

    def _cercle(self, can, x, y):
        "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
        self.cercleID = can.create_oval(x-self.r, y-self.r, x+self.r, y+self.r, fill = self.color)

    def _cercleAdaptive(self, can, x, y, a, b):
        "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
        a, b = self._getBestEllipseParameter(self.a, self.b)
        self.cercleID = can.create_oval(x-a, y-b, x+a, y+b, fill = self.color)

    def _getBestEllipseParameter(self, a, b):
        return max(self.r,a/2+3), max(self.r,b/2+3)


    def weightText(self, can, x0, y0, x1, y1, text):
        decalage = self.Angle(x0, y0, x1, y1)
        A, _ = self.thirdPts(x0+self.r*decalage[0], y0-self.r*decalage[1], x1-self.r*decalage[0], y1+self.r*decalage[1])
        #print("ligne 447", A, text)
        can.create_text(A, text=text)

    def line(self, can, x0, y0, x1, y1, r1target = 0, r2target = 0, flag=None):
        "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
        decalage = self.Angle(x0, y0, x1, y1)
        if self.arrow == True: arrow = 'last'
        else: arrow = 'none'
        aStart, bStart = self._getBestEllipseParameter(self.a, self.b)
        aTarget, bTarget = self._getBestEllipseParameter(r1target, r2target)
        if flag is None:
            can.create_line(x0+aStart*decalage[0], y0-bStart*decalage[1], x1-aTarget*decalage[0], y1+bTarget*decalage[1], arrow = arrow)
        else:
            A, _ = self.thirdPts(x0+aStart*decalage[0], y0-bStart*decalage[1], x1-aTarget*decalage[0], y1+bTarget*decalage[1])
            can.create_line(x0+aStart*decalage[0], y0-bStart*decalage[1], A, x1-aTarget*decalage[0], y1+bTarget*decalage[1], smooth=True, arrow = arrow)

    def Angle(self, x0, y0, x1, y1):
        eps = 1e-9
        return (x1-x0)/(sqrt((x0-x1)**2+(y0-y1)**2)+eps), (y0-y1)/(sqrt((x0-x1)**2+(y0-y1)**2)+eps)

    def thirdPts(self, x0,y0,x1,y1):
        xMid = (x0+x1)/2
        yMid = (y0+y1)/2
        t = atan2(y1 - y0, x1 - x0)
        return (xMid+15*sin(t), yMid-15*cos(t)), (xMid-15*sin(t), yMid+15*cos(t))

    def cerclePeint(self, color = 'white'):
        #print('ligne 27', self.text)
        if self.text != '':
            self.canev.itemconfig(self.cercleID, fill = color)
            self.color = color

""" Routines for classroom """

def parcoursLargeur(G: Noeud):
    print("DEBUT")
    f = [G]
    data = [1]
    while len(f) != 0:
        x = f.pop(0)
        print(x.valeur)
        if x.gauche != None:
            data.append(1)
            Tg = x.gauche
            f.append(Tg)
        else:
            data.append(0)
        if x.droit != None:
            data.append(1)
            Td = x.droit
            f.append(Td)
        else:
            data.append(0)
        print(x, x.valeur, x.gauche, x.droit, f)
    #print(data)


def parcoursLargeurEleve(G: Noeud):
    print("DEBUT")
    f = []
    f.append(G)
    while len(f) != 0:
        x = f.pop(0)
        print(x.valeur)
        if x.gauche != None:
            Tg = x.gauche
            f.append(Tg)
        if x.droit != None:
            Td = x.droit
            f.append(Td)
        print(x, x.valeur, x.gauche, x.droit, f)


def parcoursInfixe(a, txt, dico):
    if a is None: return
    parcoursInfixe(a.gauche, txt+'0', dico)
    print(a.valeur, txt)
    dico[a.valeur] = txt
    parcoursInfixe(a.droit, txt+'1', dico)

def parcoursInfixe2(a):
    if a is None: return
    parcoursInfixe2(a.gauche)
    print(a.valeur)
    parcoursInfixe2(a.droit)


# g = GrapheDico()
# # Exemple 1 du cours
# # g.ajouteArcs('A','B,C')
# # g.ajouteArcs('B','A,D')
# # g.ajouteArc('C','A')
# # g.ajouteArc('D','B')

# # Exemple 2 du cours
# g.ajouteArcs('A','C,D')
# g.ajouteArc('B','A')
# g.ajouteArcs('C','E,D')
# g.ajouteArcs('D','A,B,C,E,F')
# g.ajouteArc('E','F')
# g.ajouteArcs('F','D')
#g.ajouteArcs('Romain','Lemi')

# g.ajouteArcs('Alice','Bob','Cathy')
# #g.ajouteArc('Alice','Cathy')
# g.ajouteArc('Bob','Deon')
# g.ajouteArc('Kevin','Leon')
# g.ajouteArc('Leon','Alice')
# g.ajouteArc('Alice','Leon')
# g.ajouteArc('Patsy','Leon')
# g.ajouteArc('Gollum','Leon')
# g.ajouteSommet('Eleonore')


#Application(g, 'self.generateRegular', arrow = True).mainloop()
#A = Noeud(Noeud(None,"B",Noeud(None,"C",None)),"A", Noeud(Noeud(None, "E", None), "D", Noeud(Noeud(None, "H", None), "F", Noeud(None, "G", None))))
A5 = Noeud(Noeud(Noeud(Noeud(Noeud(None,"",None),"||",None),54,None),"",None),"ABC", None)
A4 = Noeud(Noeud(Noeud(None,'A',None),'B',Noeud(None,'C',None)),'D',Noeud(Noeud(None,'E',None),'F',Noeud(Noeud(None,'I',None),'G',Noeud(Noeud(None,'J',None),'H',Noeud(None,'K',None)))))
A3 = Noeud(Noeud(Noeud(None, "C", Noeud(None, "E", None)), "B", Noeud(None, "D", None)), "A", Noeud(Noeud(Noeud(None, "I", None), "G", None), "F", Noeud(None, "H", Noeud(None, "J", None))))
A2 = Noeud(Noeud(None, 'B', Noeud(None, 'C', None)), 'A', Noeud(None, 'D', None))
A = Noeud(Noeud(Noeud(None, 'D', None), 'B', Noeud(None, 'E', None)), 'A', Noeud(None, 'C', None))
#g2 = GrapheDico()

print('<<<<<<<')
parcoursInfixe2(A)
print('<<<<<<<')

def affiche(A):
    if A is None: return
    print("[", end="")
    affiche(A.gauche)
    print(A.valeur, end="")
    affiche(A.droit)
    print("]", end="")

def etatArbre(txt):
    """ counts the number of opening '[' and closing ']':
      - An opening bracket is counted as +1
      - A closing bracket is counted as -1
    """
    print(txt, len(txt))
    if len(txt) == 0: return [-100]
    return [txt[0:i+1].count('[')-txt[0:i+1].count(']') for i in range(len(txt))]

def validerArbre(txt):
    """ A tree is considered valid if :
      - the last item is 0
      - the minimum of the open/close brackets count is positive (avoid the invalid : [a][b])
    """
    """a valid tree shouldn't have two consecutive numbers !!! It can 5 4 3 2 1 ok  but 4 5 4"""
    print('toto', txt)
    return txt != '[]' and etatArbre(txt)[-1] == 0 and min(etatArbre(txt)) >= 0

def getRoot(txt):
    """ functional paradigm : groupby gathers the groups of similar values ;
    enumerate gives us a list of indices ; the filter selects the longest streak of brackets
    equal to 1 (i.e. the root of the sub-tree)
        returns a list of indices corresponding to the root of the sub-tree.
    """
    # si pas de lettres dans les [], problème !!!
    tab = etatArbre(txt)
    print("error", txt, len(txt), tab)
    groups = [list(g) for _, g in groupby(enumerate(tab), lambda x: x[1])]
    print(groups)
    l = list(filter(lambda g : g[0][1]==1 and len(g)>=2, groups))[0][1:]
    print('ici', txt, [i for i, _ in l])
    return [i for i, _ in l]

def construireArbre(txt):
    """ build recursively node by node the binary tree """
    if not validerArbre(txt): return #Noeud(None,"none",None)  # is it a validTree ?
    liste = getRoot(txt)
    return Noeud(construireArbre(txt[1:liste[0]]), txt[liste[0]:liste[-1]+1], \
                 construireArbre(txt[liste[-1]+1:len(txt)-1]))

def autocompletion(txt):
    txtAutoCompleted = ''
    i = 0
    while i<len(txt):
        j=0
        while txt[i+j] != '[' and txt[i+j] != ']':
            j+=1
        if txt[i-1] == '[' and txt[i+j] == ']':
            txtAutoCompleted += '[none]' + txt[i:i+j] + '[none]]'
        else:
            j = 0
            txtAutoCompleted += txt[i]
        i += j+1
    return getSingle(getSingle(txtAutoCompleted,'['),']')


def getSingle(txt, char):
    """ detect single node and add a second empty (None) node """
    save = []
    saveA = []
    tab = ''
    pos = 0
    if char == '[': char1 = ']' 
    else: char1 = '['
    for i in txt:
        if i == char:
            if tab != '' and char1 not in tab: 
                save.append(tab)
                saveA.append(pos)
            tab = ''
        else : 
            tab += i
        pos += 1
    print('ligne 552',save)

    if char == '[': save2 = [saveA[i]-len(save[i]) for i in range(len(save))]
    else : save2 = [saveA[i]-len(save[i])+len(save[i]) for i in range(len(save))]

#    print('ligne 557', save2, [saveA[i]-len(save[i]) for i in range(len(save))], txt)

    if len(save2) == 0 : return txt
    txtAutoCompleted = ''
    j = 0
    for i in range(len(save2)):
        while j < save2[i]:
            txtAutoCompleted += txt[j]
            j += 1
        txtAutoCompleted += '[none]'
    print('ligne 431',char, save2)
    print(txtAutoCompleted)
    txtAutoCompleted += txt[save2[-1]:]
    return txtAutoCompleted

def colorationDSATUR(G):
    sommetsOrd = sorted(G.listeSommets(), key = lambda x: G.degre(x), reverse =True)
    couleur = {}
    degreMax = sommetsOrd.pop(0)
    couleur[degreMax] = 0 

    while sommetsOrd != []:
        maxDSAT = dsat(G, couleur)

        sommet2color = egalite(sommetsOrd, maxDSAT)

        # remplacez ces lignes par une instruction Python sur les tableaux.
        for i, liste in enumerate(sommetsOrd):
            if liste[0] == sommet2color:
                iPop = i
        print('ipo', iPop)

        aColorier = sommetsOrd.pop(iPop)
        print('acol',aColorier)
        couleur[aColorier] = choixCouleur(G, aColorier, couleur)
    return couleur


# def colorationG12(G: GrapheDico):
#     couleurTab = list(range(50))
#     couleurDico = {}
#     S = G.listeSommets()
#     for sommet in S:
#         couleursVoisins = [couleurDico[s] for s in G.listeVoisins(sommet) if s in couleurDico]            
#         nf = True
#         for i in couleurTab:
#             if i not in couleursVoisins and nf == True:
#                 pc = i 
#                 nf = False
#         couleurDico[sommet] = pc
#     return dic

def colorationG1(G):
    couleurTab = list(range(50))
    couleurDico = {}
    S = G.listeSommets()
    for sommet in S:
        couleursVoisins = [couleurDico[s] for s in G.listeVoisins(sommet) if s in couleurDico]            
        couleurDico[sommet] = pc(couleurTab, couleursVoisins)
    return couleurDico

def pc(couleurTab, couleursVoisins, n = 50):
    for i in list(range(n)):
        if i not in couleursVoisins:
            return i

def colorationG1p(G):
    listeCouleur = list(range(10))
    dic = {}
    S = sorted(G.listeSommets(), key = G.degre, reverse=True)
    for sommet in S:
        couleursVoisins = [dic[s] for s in G.listeVoisins(sommet) if s in dic]            
        nf = True
        for i in listeCouleur:
            if i not in couleursVoisins and nf == True:
                pc = i 
                nf = False
        dic[sommet] = pc
    return dic

def choixCouleur(G, sommet, couleur, n=10):
    A = {couleur[i] for i in G.listeVoisins(sommet) if i in couleur}
    print('A',A)
    for j in range(n):
        if j not in A:
            return j
    raise Exception('Please increase number of colors')

def egalite(sommetsOrd, maxDSAT):
    cles = [i for i in maxDSAT]
    for sommet in sommetsOrd:
        if sommet in cles:
            return sommet[0]
    raise Exception('Something went wrong')

def dsat(G, couleurTab):
    degreSat = {i:set() for i in G.listeSommets()}
    for sommet in couleurTab:
        for i in G.listeVoisins(sommet):
            degreSat[i].add(couleurTab[sommet])
    return trouveMax({s: len(couleur) for s, couleur in degreSat.items() if s not in couleurTab})

def trouveMax(dico):
    maxi = -1
    for cle, valeur in dico.items():
        if maxi < valeur:
            maxVal = [cle]
            maxi = valeur
        elif maxi == valeur:
            maxVal.append(cle)
    return maxVal
            
