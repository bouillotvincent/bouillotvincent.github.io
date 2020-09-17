def calcul(op, t):
    """ calcule t[O] op t[1] op ... t[n-1],
    le tableau t étant supposé non vide"""
    v = t[0]
    for i in range(1, len(t)):
        v = op(v, t[i])
        print(op, v, t[i])
    return v