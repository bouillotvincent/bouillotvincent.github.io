def insere(inf, L: list, i: int, v: float)-> list:	
    j = i	
    while j>0 and inf(v, L[j-1]):
        L[j] = L[j-1]	
        j = j-1	
        print(j, v, L[j-1])
    L[j] = v	

def triInsertion(inf, t: list):
    for i in range(1, len(t)):	
        insere(inf, t, i, t[i])

def inf1(x:float, y: float):
    return x < y

def inf2(x:float, y: float):
    return x > y

"""" A faire vous meme 6"""
def inf3(x: list, y:list):
    return x[1] < y[1]

def infUltime(x, y):
    if isinstance(x, list):
        return inf3(x,y)
    else:
        return inf1(x,y)


t = [2,1,4,-1]
grosT = [[2,10,1,-1], [5,1,4,-1], [2,1,3,-1], [8,3,2,-1], [8,1,5,-1]] 

triInsertion(infUltime, t)
triInsertion((lambda x, y: x[1]<y[1]) , grosT)
print(grosT)
print(t)
#triInsertion(inf2, t)
#print('reverse', t)
