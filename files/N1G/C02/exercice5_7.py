def estBinaire(nbin):
    """ 
    Teste si une chaine de caractères nbin
    est compatible avec notre format binaire 
    Par exemple : 0b01011
    """
    prefix = nbin[0:2] # caractère '0b' si existant
    nbin = nbin[2:]    # "nombre binaire" à tester

    if 'à compléter':
        return 
    else:
        for bit in 'à compléter':
           return 
        return 

def bin2dec(nbin):
    """ 
    Convertit un nombre binaire en base 10
    """
    nbin = nbin[2:]   # nombre binaire
    L = len(nbin)-1

    for bit in nbin:
        nombreDec = ''
        L = ''
    assert(nombreDec == int(nbin,2))  # test : le nombre trouvé est-il le nombre attendu?
    return nombreDec

def dec2bin(n):
    """ 
    Convertit un nombre n écrit en base 10 
    en un nombre nBin écrit en base 2
    """   
    nBin = ''

    assert(str(bin(int(n))) == int(nBin,2))
    return nBin


if __name__ == '__main__':

    val = '0b21210011'  # chaine à tester
    print(val + 'est un nombre binaire valide.', estBinaire(val)) # doit être False
    assert(estBinaire(val)==False)

    val = '0b012210011'  # chaine à tester
    print(val + 'est un nombre binaire valide.', estBinaire(val)) # doit être False
    assert(estBinaire(val)==False)

    val = '0x01010011'  # chaine à tester
    print(val + 'est un nombre binaire valide.', estBinaire(val)) # doit être False
    assert(estBinaire(val)==False)

    val = '2201010011'  # chaine à tester
    print(val + 'est un nombre binaire valide.', estBinaire(val)) # doit être False
    assert(estBinaire(val)==False)

    val = '0b01010011'  # chaine à tester
    print(val + 'est un nombre binaire valide.', estBinaire(val)) # doit être True
    assert(estBinaire(val)==True)

    val = '0b1011'
    print(bin2dec(val))