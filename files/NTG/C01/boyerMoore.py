import time

texte = 'CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTACGGTAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTT'
motif = "CGGCAG"

#texte = 'abracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaaraabracadabrararararaaara'
#motif = "ra"

#texte = 'bricabrac'
#motif = 'bra'

# texte = """Les Fleurs du Mal
# En juillet 1857, Charles Baudelaire publie son œuvre majeure : Les Fleurs du Mal. Ce recueil de poèmes est condamné "pour outrage à la morale publique et aux bonnes mœurs". Baudelaire et son éditeur doivent payer une lourde amende. Une nouvelle édition est produite en 1861, d'où sont supprimées six poèmes conformément au jugement prononcé. Une demande de réhabilitation des Fleurs du Mal devant la cour de cassation aboutira le 30 mai 1949, longtemps après sa mort, et annulera la précédente condamnation. Dans Les Fleurs du Mal, Baudelaire met en lumière la dualité entre la violence et la volupté, le bien et le mal, la laideur et la beauté, l'enfer et le ciel...

# La mort de Charles Baudelaire
# Croulant sous les dettes, Baudelaire part en Belgique pour y donner des conférences. Dans un premier temps plein d'espoir pour ce nouveau départ, il est vite déçu par cette expérience. Baudelaire séjournera en Belgique de 1864 à 1866, date à laquelle le poète commence à avoir de sérieux problèmes de santé (syphilis, perte de la parole…). Il retourne à Paris en juillet 1866. Il s'y éteint un an plus tard, le 31 août 1867, à l'âge de 46 ans, des suites de la syphilis, de l'abus d'alcool et autres drogues. En 1868 sont publiés à titre posthume Le Spleen de Paris (recueil de poèmes en prose) et les Curiosités esthétiques.

# Le spleen selon Charles Baudelaire
# Dans Les Fleurs du Mal, Charles Baudelaire intitule la première partie de son recueil : Spleen et idéal. Les poèmes qui y sont regroupés présentent l'ennui et la mélancolie que lui inspire la vie quotidienne. Quatre d'entre eux portent également le nom de Spleen. Dans l'œuvre de Baudelaire, le "spleen" est un mal-être, une immense tristesse, une forme de dépression du poète. Entre 1855 et 1864, Charles rédige une série de poèmes en prose pour différents titres de presse. Ils seront regroupés sous le titre de Spleen de Paris et publiés après sa mort. Tiré de ses lectures étrangères, Charles Baudelaire s'est approprié le mot pour en faire le fil conducteur de son œuvre. Après lui, d'autres artistes ont utilisé le spleen tel que Paul Verlaine dans Romances sans paroles."""


#texte = "abracadabracadabricadabra"
#motif = "adabrica"

def recherche0(m, t):
    """affiche toutes les occurrences de m dans t"""
    lenMotif = len(m)
    lenTexte = len(t)
    for s in range(lenTexte-lenMotif+1):
        if t[s:s+lenMotif] == m:
            print("occurrence à la position", s)


def occurrence1(m, t, s):
    """indique s'il y a occurrence de la chaine m dans la chaine t à la position s"""
    if not(0 <= s <= (len(t)-len(m))): return False
    for j in range(len(m)):
        if t[s+j] != m[j]: return False
    return True

def recherche1(m, t):
    """affiche toutes les occurrences de m dans t"""
    lenMotif = len(m)
    lenTexte = len(t)
    for s in range(lenTexte-lenMotif+1):
        if occurrence1(m, t, s): 
            print("occurrence à la position", s)

def occurrence2(m, t, s):
    """indique l'existence d'une occurrence.
    Si pas d'occurrence complète, checkLetter2 indique si 
    la t[s+j]-ième lettre du texte apparait dans le motif.
    """
    if not(0 <= s <= (len(t)-len(m))): 
        return False
    for j in range(len(m)-1,-1,-1):
        if t[s+j] != m[j] :
            return False, j, checkLetter2(t[s+j], m)
    return True, s, None

def checkLetter2(lettre, m):
    """renvoie True si lettre est dans m et False sinon. 
    La fonction native 'in' de Python n'est pas utilisée.
    """
    for car in m:
        if lettre == car:
            return True
    return False

def decalage2(lettre, m, j):
    """calcule le décalage d'une lettre dans un mot m entre les indices [0;j].
    Si la lettre est présente dans le mot mais pas dans l'intervalle [0;j], 
    on renvoie -1.
    """
    for i in range(j, -1, -1):
        if lettre == m[i]:
            return i
    return -1

def recherche2(m, t):
    """affiche toutes les occurrences de m dans t"""
    lenMotif, lenTexte = len(m), len(t)
    s = 0
    dico = [{i: 'NA'} for i in m]
    while s <= lenTexte - lenMotif:
        isOccurrence, j, isIn  = occurrence2(m, t, s)
        if isOccurrence: 
            print("occurrence à la position", s)
            s += 1
        else:
            k = s + j
            if not isIn : s = k+1
            else : 
                dec = decalage2(t[k], m, j) 
                if decalage2(t[k], m, j) == -1 : dec = 0
                dico[j][t[k]] = decalage2(t[k],m,j)
                s += lenMotif - dec - 1
    afficheTable(dico)

def afficheTable(dico):
    a=[f'{str(i): >5.4}' for i in list(dico[-1].keys())]
    print(*a)
    for i, u in enumerate(dico):
        a=[f'{str(u[j]): >5.4}' if j in u.keys() else f'{str(""): >5.4}' for j in list(dico[-1].keys())]
        print(i, *a)


def tableBM(m):
    """Construit la table de positions de Boyer-Moore
    d[j][c] est le plus grand k<j tel que m[k] == c,
    s'il existe, et n'est pas défini sinon"""
    dico = [ {} for _ in range(len(m))]
    for j in range(len(m)):
        for i in range(j):
            dico[j][m[i]]= i
    return dico

def decalage(table, j, lettre):
    """ utilise la table table lorsque le caractère 
    numéro j est lettre au lieu du caractère attendu"""
    if lettre in table[j]:
        print('lettre dans motif')
        return j - table[j][lettre]
    else:
        print('lettre absente')
        return j+1

def rechercheBM(m, t):
    """affiche toutes les occurrences de m dans t avec l'algorithme
    de Boyer-Moore"""
    table = tableBM(m)
    s = 0
    while s <= len(t) - len(m):
        ncomp = 0
        dec = 0
        for j in range(len(m)-1, -1, -1):
            ncomp += 1
            if t[s+j] != m[j]:
                dec = decalage(table, j, t[s+j])
                break
        if dec == 0:
            print("occurrence à la position", s)
            dec = 1
        print(f"s, {s}, decalage, {dec}, nombre de comparaisons {ncomp}")
        s += dec
        
#afficheTable(tableBM(motif))
texte = 'abcdcherecherzzplutonaachychercherchera'
motif = 'chercher'
rechercheBM(motif, texte)