# Golfed Version
def H(o):O=ord;G=len(o);p=[[' ―'[O(i)<O(g)],'|'][O(i)>O(g)]for i in o for g in o];u='\n'.join([''.join(p[i:G+i]+p[i:G+i][::-1])for i in range(0,len(p),G)]);print(u+'\n'+u[::-1])
H('rkap')

# Ungolfed Version
def H(o):
    O=ord
    G=len(o)
    p=[[' ―'[O(i)<O(g)],'|'][O(i)>O(g)]for i in o for g in o]
    u='\n'.join([''.join(p[i:G+i]+p[i:G+i][::-1])for i in range(0,len(p),G)])
    print(u+'\n'+u[::-1])

