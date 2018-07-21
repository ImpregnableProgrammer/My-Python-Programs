# This Challenge: http://codegolf.stackexchange.com/questions/85302/find-the-paths

def G1(i):
    J=[*i]
    print(J)
    for u in range(len(J)-12):
        if J[u]!='\n'and J[u]!=' ':
            if J[u]==J[u+6]:
                J[u]=J[u+6]='x'
            elif J[u]==J[u+1]:
                print(J[u],J[u+1],u)
                J[u]=J[u+1]='x'
    print(J)
    print(''.join(J))

def G(i):
    T=[*i]
    for u in range(1,len(i)-6):
        if (T[u-1]==T[u]or T[u-6]==T[u])and T[u] not in[' ','\n']:
            T[u]='x'
    print(''.join(T))

G('''12 45
11233
  233
    1
2 899''')

print('\n')
import re;print(re.sub(r'(\w).+?\1','x','''12 45
11233
  233
    1
2 899''',re.DOTALL))



