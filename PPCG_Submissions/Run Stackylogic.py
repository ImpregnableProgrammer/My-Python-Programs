# This Challenge:
def H(o):
    o=o.split('\n');print(o);Q=[];i=0
    for z in o:
        i+=1
        if'<'in z:
           print(z)
           try:
               if z[-2]=='0':
                   o[i][i-1]+='<'
               elif z[-2]=='1':
                   o[i][i+1]+='<'
               elif z[-2]=='?':
                   o[i].replace('?',input())
           except:
               break
           Q.append(o[i][-2])
           o[i]=o[:-1]
           i=0
    print(o)
    print(Q.pop())

H('''1
?<
11
?
0''')


