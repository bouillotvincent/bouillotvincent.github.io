
laClasse = [("Zoé", 17), ("Jed", 14),("Léo", 15), ("Noé", 16), ("Ana", 18), ("Max", 18), ("Lin", 17), ("Robert", 44)]

# Aide avec les indices : 
print(laClasse[0]) # affiche le premier élève du tableau : ("Zoé", 17)
print(laClasse[0][0]) # affiche le premier attribut du premier élève du tableau : "Zoé"

def comptage(T: list)-> int:
    '''
    Cette fonction compte le nombre d'élèves ayant moins de 16 ans.
    T : tableau d'élève d'une classe au format [(nom1, age1), (nom2, age2) ...]
    Renvoie un entier.
    '''
    # A Completer
    # ....
    # ....
    return # A Completer


def preAdo(T: list)-> str:
    '''
    A compléter
    '''
    # A Completer
    # ....
    # ....
    return # A Completer

def grosFreak(T: list)-> int:
    '''
    A compléter
    '''
    # A Completer
    # ....
    # ....
    return # A Completer


print(comptage(laClasse))




from matplotlib.pyplot import *
import string
import random

alphabet = list(string.ascii_uppercase)

data = "EAGHQZF, BAGD E’MYGEQD, XQE TAYYQE P’QCGUBMSQ BDQZZQZF PQE MXNMFDAE, HMEFQE AUEQMGJ PQE YQDE,CGU EGUHQZF, UZPAXQZFE OAYBMSZAZE PQ HAKMSQ,XQ ZMHUDQ SXUEEMZF EGD XQE SAGRRDQE MYQDE." \
     +"M BQUZQ XQE AZF-UXE PQBAEQE EGD XQE BXMZOTQE,CGQ OQE DAUE PQ X’MLGD, YMXMPDAUFE QF TAZFQGJ,XMUEEQZF BUFQGEQYQZF XQGDE SDMZPQE MUXQE NXMZOTQEOAYYQ PQE MHUDAZE FDMUZQD M OAFQ P’QGJ." \
     +"OQ HAKMSQGD MUXQ, OAYYQ UX QEF SMGOTQ QF HQGXQ!XGU, ZMSGQDQ EU NQMG, CG’UX QEF OAYUCGQ QF XMUP!X’GZ MSMOQ EAZ NQO MHQO GZ NDGXQ-SGQGXQ,X’MGFDQ YUYQ, QZ NAUFMZF, X’UZRUDYQ CGU HAXMUF!" \
     +"XQ BAQFQ QEF EQYNXMNXQ MG BDUZOQ PQE ZGQQECGU TMZFQ XM FQYBQFQ QF EQ DUF PQ X’MDOTQD;QJUXQ EGD XQ EAX MG YUXUQG PQE TGQQE,EQE MUXQE PQ SQMZF X’QYBQOTQZF PQ YMDOTQD."

x = [i for i in range(len(alphabet))]
# y = tableau à créer pour faire un histogramme...
# Exemple ci-dessous
y = [random.randint(1,20) for i in range(len(alphabet)) ]

bar(x, y, tick_label=alphabet)
show()