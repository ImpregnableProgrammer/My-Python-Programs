# This Challenge: http://codegolf.stackexchange.com/questions/84592/compute-the-maximum-number-of-runs-possible-for-as-large-a-string-as-possible

# Python Lambda Regular Expression to check if a given string is periodic; Works
import re
S=lambda T:bool(re.search(r'(\w).{0,%s}\1+'%str((len(T)//2)-1),T))
print(S('ababababa'))

def T(p):
    o=1;q=0
    for u in range(len(p)-1):
        print('u:',u)
        for y in range(u+2,len(p)+1):
            print('y:',y)
            print(p[u:y])
T('0011')

