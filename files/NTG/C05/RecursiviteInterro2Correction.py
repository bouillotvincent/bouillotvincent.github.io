def mystere(t, i): 	
    if i == 0: 	
        return 0 	
    else: 	
        return t[i-1]<t[i] + mystere(t,i-1) 	

print(mystere([10,9,11,42],3))

def Ack(m, n):
    assert m>=0 and n>=0, 'm et n ne peuvent pas être négatifs'
    if m==0: return n+1
    elif n==0: return Ack(m-1,1)
    elif n>0: return Ack(m-1, Ack(m, n-1))

print(Ack(0,1))
print(Ack(0,2))
print(Ack(1,0))
print(Ack(2,0))
print(Ack(1,2))