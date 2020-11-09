def mystere(t, i): 	
    if i == 0: 	
        return 0 	
    else: 	
        return t[i-1] + mystere(t,i-1) 	

print(mystere([10,9,11,42],3))

def pgcd(a, b):
    print(a, b)
    return (a if b==0 else pgcd(b, a%b))
    if b == 0:
        return a 
    return pgcd(b, a%b)

print(pgcd(120,36))

def produitDesChiffres(n): 
    if n<=9:
        return n 
    else:
        return n%10 * produitDesChiffres(n//10)

print(produitDesChiffres(249))