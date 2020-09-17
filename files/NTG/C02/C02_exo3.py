def insere(L: list, i: int, v: float)-> list:	
    j = i	
    while j>0 and v < L[j-1]:
        L[j] = L[j-1]	
        j = j-1	
        print(j, v, L[j-1])
    L[j] = v	
	
def triInsertion(t: list):
    for i in range(1, len(t)):	
        insere(t, i, t[i])

t = [2,1,4,-1]
grosT = [[2,10,1,-1], [5,1,4,-1], [2,1,3,-1], [8,3,2,-1], [8,1,5,-1]] 
print(t)