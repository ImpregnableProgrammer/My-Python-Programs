# This Challenge: http://codegolf.stackexchange.com/questions/86746/verify-a-tower-of-hanoi-solution#86750

# Python 3 version at 137 bytes
a,b=eval(input());Q=range(1,-~a)[::-1];U=[[*Q],[],[]]
for K,J in b:U[J]+=[U[K].pop()]if U[J]<[1]or U[K]<U[J]else Y
print(U[-1]==[*Q])

# Final Version Golfed in Python 2.7 at 127 bytes
# r=range;a,b=input();U=[r(a,0,-1),[],[]]
# for K,J in b:U[J]+=[U[K].pop()]if U[J]<[1]or U[K]<U[J]else Y
# print U[-1]==r(a,0,-1)

