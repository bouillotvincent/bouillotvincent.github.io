n = input('Entrez un dividende : ')
q = input('Entrez un diviseur : ')

def DE(n, q):
    """
    DE fait une division euclidienne du pauvre
    """
    # vérification que n et q sont des entiers
    assert type(n) is int 
    assert type(q) is int 

    r = n
    p = 0
    while r>=q:
        r = r-q
        p = p+1
    return p, r

a, b = DE(n, q)

print(a, b)
#print('Le quotient vaut ' + a + ' et le reste vaut ' + b)