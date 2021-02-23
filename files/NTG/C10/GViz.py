"""
Bibliothèque GViz
Auteur : Vincent BOUILLOT
Version actuelle : 1.11
Date : Février 2020
"""

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
    """
        Permet de représentation graphiquement des graphes et des arbres binaires grâce à Tkinter.
        Gère de manière dynamique les sommets d'un Graphe par un click and drag.

        Paramètres d'entrée : 
            - G : objet de la classe GrapheDico
        
        Paramètres optionnels [Defaults] : 
            - arrow [True] : 
                True / Graphe orienté 
                False / Graphe non-orienté
            - width [500] :
                Largeur de la fenêtre graphique
            - height [500] :
                Hauteur de la fenêtre graphique
            - weight [False] -- non pris en compte dans les méthodes du cours :
                True / Graphe pondéré 
                False / Graphe non-pondéré

        Exemple d'utilisation pour un graphe appelé G :
            Application(G, arrow = True, width=500, height=300).mainloop()
    """

    _color = 255

    def __init__(self, G, arrow = True, width = 500, height = 500, weight = False):
        Tk.__init__(self)        # constructeur de la classe parente
        self.can = Canvas(self, width = width, height = height, bg ="white")
        self.can.grid(row = 2, column = 0, columnspan = 3)
        self.can.update()
        self.a = {}
        self.params = G
        self.weight = weight
        self.flag = False
        # if G is a Node (ie binary tree), don't show arrows
        if not isinstance(G, Noeud): self.arrow = arrow
        else: self.arrow = False
        self.move = ''
        self.connect = []
        self.dessine(G, self.generateRegular )
        self.can.bind('<Button-1>', self.startMove)
        self.can.bind('<Motion>', self.hover)
        self.can.bind('<ButtonRelease-1>', self.stopMove)
        # self.can.bind('<Button-3>', self.startConnect)
        # self.can.bind('<ButtonRelease-3>', self.stopConnect)
        Button(self, text = "Polygone Regulier", command = lambda x=3: self.dessine(G,self.generateRegular)).grid(row = 3, column = 0)
        Button(self, text = "Grille", command = lambda x=3: self.dessine(G,self.generateGrid)).grid(row = 3, column = 1)
        Button(self, text = "Parcours préfixe", command = lambda x=3: self.drawParcours(self.params[0], 'préfixe')).grid(row = 3, column = 2)
        Button(self, text = "Parcours infixe", command = lambda x=3: self.drawParcours(self.params[0], 'infixe')).grid(row = 3, column = 3)
        Button(self, text = "Parcours suffixe", command = lambda x=3: self.drawParcours(self.params[0], 'suffixe')).grid(row = 3, column = 4)
        okCmd = self.can.register(self.callback)
        self.sv = StringVar()
        self.ent = Entry(self, textvariable = self.sv, validate = "all", validatecommand = (okCmd, '%P'))
        self.ent.grid(row = 4, column = 0, columnspan = 4, sticky='EW', padx = 20)
        # self.lab = Label(self, text = '')
        # self.lab.grid(row = 4, column = 5)

    def callback(self, value):
        #self.ent.configure(text = self.sv + 'z')
        if validerArbre(value):
            self.params[0] = construireArbre(value)
            print('155', self.params[0])
            if self.params[0] is not None:
                self.a = {}
                self.dessine(self.params[0], eval('self.' + self.params[1]))
            return True
        else: return True


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

    def moveTo(self, x, y, r = 15):
        """ 
        Nouvelles coordonnées pour le noeud déplacé
        Mise à jour de la fenêtre graphique
        """
        self.a[self.move].x = x
        self.a[self.move].y = y
        G = self.params
        self.dessine(G, self.generateRegular )

    def taille(self, G):
        if G is None : return 0
        return 1 + self.taille(G.gauche) + self.taille(G.droit)

    def hauteur(self, G):
        if G is None : return 0
        return 1 + max(self.hauteur(G.gauche), self.hauteur(G.droit))
    
    def listeFils(self, noeud, dico):
        base = dico[noeud]
        fils = []
        for key, value in dico.items():
            if value == base + '0' or value == base + '1':
                fils.append(key)
        return fils       

    def dessine(self, G, func):
        self.can.delete('all')
        if not isinstance(G, Noeud) : # Graph entered as a dictionnary
            print(self.move, len(self.move), not len(self.move))
            if not len(self.move):  
                # First generation of coordinates following the rules defined by func
                listCoords = func(len(G.listeSommets()))
                #Create GraphViz objects
                for i,text in enumerate(G.listeSommets()):
                    self.a[text] = graphViz(self.can, listCoords[i][0], listCoords[i][1], text, G.listeVoisins(text), self.arrow)
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
                    if G.isDoubleArc(text, sommet) and self.arrow: 
                        self.flag = not self.flag
                        self.a[text].line(self.can,self.a[text].x,self.a[text].y, self.a[sommet].x,self.a[sommet].y, self.flag)
                    else: 
                        self.a[text].line(self.can,self.a[text].x,self.a[text].y, self.a[sommet].x,self.a[sommet].y)

                    if self.weight:
                        local.append((text, sommet))
                        if (sommet, text) not in local:
                            self.a[text].weightText(self.can,self.a[text].x,self.a[text].y, self.a[sommet].x,self.a[sommet].y,G.listeVoisins(text)[sommet])    

        else: # Binary tree entered as Nodes
            dico = {}
            self.parcoursInfixe(G, '', dico)
            if not len(self.move):
                # First generation of coordinates following the rules defined by func
                listCoords = self.generateTree(self.hauteur(G))[::-1]
                listIndex = [self._bin2index(dico[i]) for i in self.parcoursLargeur(G)]
                coords = [listCoords[i] for i in listIndex]
            else:
                # Redefinition of coordinates following a click-and-drag
                coords = [(self.a[text].x, self.a[text].y) for text in self.a]
            #print('Paris', dico)
            dico = self.triage(dico)
            print(dico)
            for i, text in enumerate(dico.keys()):
                self.a[text] = graphViz(self.can, coords[i][0], coords[i][1], text, self.listeFils(text, dico), self.arrow)

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
    

    def parcoursLargeur(self, G):
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
        length = 75    
        return [(i*length % w+50,  j*length % h+50) for i in range((w-50) // length) for j in range((h-50) // length)]

    def parcoursInfixe(self, a, txt, dico):
        if a is None: return
        self.parcoursInfixe(a.gauche, txt+'0', dico)
        while a.valeur in dico: 
            a.valeur += '.'
        dico[a.valeur] = txt
        self.parcoursInfixe(a.droit, txt+'1', dico)

    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   

    def drawParcours(self, arbre, type = "infixe", call = 1):
        if not call : 
            self.clearColor()
        if arbre is None: return
        print(type)
        if type == "préfixe":self._animatePaint(arbre)
        self.drawParcours(arbre.gauche, type )
        if type == "infixe": self._animatePaint(arbre)
        self.drawParcours(arbre.droit, type)
        if type == "suffixe": self._animatePaint(arbre)

    def clearColor(self):
        """ to maintain """
        for i in self.a:
            print(i)
            self.a[i].cerclePeint(color = self._from_rgb((0, 0, 0)))
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
    def __init__(self, canev, x, y, text, voisins, arrow, color = 'white', rayon = 15):
        self.canev, self.x, self.y, self.voisins, self.arrow = canev, x, y, voisins, arrow
        self.text = text
        self.r = rayon
        self.cercleID = 0
        self.color = color

    def cercles(self, canev, x, y):
        self._cercle(canev, x, y)
        self.canev.create_text(x, y, text=self.text)

    def _cercle(self, can, x, y):
        "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
        self.cercleID = can.create_oval(x-self.r, y-self.r, x+self.r, y+self.r, fill = self.color)

    def weightText(self, can, x0, y0, x1, y1, text):
        decalage = self.Angle(x0, y0, x1, y1)
        A, _ = self.thirdPts(x0+self.r*decalage[0], y0-self.r*decalage[1], x1-self.r*decalage[0], y1+self.r*decalage[1])
        can.create_text(A, text=text)

    def line(self, can, x0, y0, x1, y1, flag=None):
        "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
        decalage = self.Angle(x0, y0, x1, y1)
        if self.arrow == True: arrow = 'last'
        else: arrow = 'none'
        if flag is None:
            can.create_line(x0+self.r*decalage[0], y0-self.r*decalage[1], x1-self.r*decalage[0], y1+self.r*decalage[1], arrow = arrow)
        else:
            A, _ = self.thirdPts(x0+self.r*decalage[0], y0-self.r*decalage[1], x1-self.r*decalage[0], y1+self.r*decalage[1])
            can.create_line(x0+self.r*decalage[0], y0-self.r*decalage[1], A, x1-self.r*decalage[0], y1+self.r*decalage[1], smooth=True, arrow = arrow)

    def Angle(self, x0, y0, x1, y1):
        eps = 1e-9
        return (x1-x0)/(sqrt((x0-x1)**2+(y0-y1)**2)+eps), (y0-y1)/(sqrt((x0-x1)**2+(y0-y1)**2)+eps)

    def thirdPts(self, x0,y0,x1,y1):
        xMid = (x0+x1)/2
        yMid = (y0+y1)/2
        t = atan2(y1 - y0, x1 - x0)
        return (xMid+15*sin(t), yMid-15*cos(t)), (xMid-15*sin(t), yMid+15*cos(t))

    def cerclePeint(self, color = 'white'):
        print('ligne 27', self.text)
        if self.text != '':
            self.canev.itemconfig(self.cercleID, fill = color)
            self.color = color


if __name__ == "__main__":
    """ Routines for classroom """

    def parcoursLargeur(G):
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
        if len(txt) == 0: return [-100]
        return [txt[0:i+1].count('[')-txt[0:i+1].count(']') for i in range(len(txt))]

    def validerArbre(txt):
        """ A tree is considered valid if :
        - the last item is 0
        - the minimum of the open/close brackets count is positive (avoid the invalid : [a][b])
        """
        return etatArbre(txt)[-1] == 0 and min(etatArbre(txt)) >= 0

    def getRoot(txt):
        """ functional paradigm : groupby gathers the groups of similar values ;
        enumerate gives us a list of indices ; the filter selects the longest streak of brackets
        equal to 1 (i.e. the root of the sub-tree)
            returns a list of indices corresponding to the root of the sub-tree.
        """
        tab = etatArbre(txt)
        groups = [list(g) for _, g in groupby(enumerate(tab), lambda x: x[1])]
        l = list(filter(lambda g : g[0][1]==1 and len(g)>=2, groups))[0][1:]
        return [i for i, _ in l]

    def construireArbre(txt):
        """ build recursively node by node the binary tree """
        if not validerArbre(txt): return   # is it a validTree ?
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



    print('là',autocompletion('[A[[ABL]CL[AB[I]]]]'))


    B = construireArbre('[[[D]B[E]]A[C]]')
    C = construireArbre('[[E[[J]F[G]]]A[[[[K]D[L]]C]B[M]]]')
    D = construireArbre('[[[D]B[E]]A[C]]')

    # print("method getIndex",[w for w in getIndex('[[B0[EL]]A[[ABL[CC]]CL]]', '[')])
    # print("method getIndex",[w for w in getIndex('[[B0[EL]]A[[ABL[CC]]CL]]', ']')])

    print('-----')
    getSingle('[[B0[EL]]A[[ABL[CC]]CL]]', '[')
    print('-----')
    getSingle('[[B0[EL]]A[[ABL[CC]]CL]]', ']')
    print('-----')
    getSingle(getSingle('[[B0[EL]]A[[ABL[CC]]CL]]', ']'),'[')
    print('-----')


    affiche(A)
    print()
    affiche(B)

    print('ici', parcoursLargeur(A2))

    #D = construireArbre('[[none]A[[none]B[[none]C[[none]D[none]]]]]')
    D = construireArbre(('[[[[[1]5]10[11]]21[[22[11]]30[45]]]55[[[59]60[67]]89[[92]121[132]]]]'))
    #a=construireArbre(autocompletion('[[B0[EL[KK]]]A[[ABL[CC]]CL[AB[I]]]]'))  # Problème with node AB
    print('là',autocompletion('[[B0]A[[ABL]CL[AB[I]]]]'))
    a=construireArbre(autocompletion('[[B0]A[[ABL]CL[AB[I]]]]'))  # Problème with node AB
    #D=construireArbre(autocompletion('[B0[[[DG]K]A[AV[A]]]]'))
    #print('ligne',a)
    #D = construireArbre(a)
    #print('ligne 463',D)
    #D = construireArbre(autocompletion('[[[none]B0[EL]]A[[[none]ABL[CC]]CL]]'))
    #detectSingleNode('[[BO[EF]]AB[[KL]CM]]')
    #g2.arbre2Graph(g2.createArbreParfait(A))
    #print(g2.adj)
    #print('ligne321',g2.adj)
    #print(g2.distanceMax('A'))
    g = GrapheDico()
    g.ajouteArcs('A', 'B,C,E')
    g.ajouteArcs('C', 'A,F')
    g.ajouteArcs('B', 'D')
    g.ajouteArcs('D', 'B,C,A')
    for i in range(10):
        g.ajouteArcs('D', 'B,C,A')
    #g.showAdjMatrixLTX()
    #g.showAdjMatLTX()
    print(g.distance('A','F'))
    D = construireArbre("[A]")
    Application(g, 'generateRegular', weight = True, arrow = False, width=500, height=300).mainloop()
    #Application(g, 'generateRegular', arrow = False, width=500, height=300).mainloop()



    a = ABR()
    a.ajouter(30)
    a.ajouter(40)
    a.ajouter(10)
    a.ajouter(35)
    print(a.racine.gauche.valeur,a.racine.droit.valeur,a.racine.droit.gauche.valeur)