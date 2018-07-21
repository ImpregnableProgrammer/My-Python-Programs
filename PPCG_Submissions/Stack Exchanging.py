# The Challenge: http://codegolf.stackexchange.com/questions/80961/stack-exchanging


def J(j):
    q={i:[i]*j for i in range(1,j+1)};print(q)
    while any(q[i]!=[*range(1,j+1)]for i in q.keys()):
        if q[j].count(j)>1:
            if any(len(q[i])<1for i in range(1,j+1)):
                [q[i]for i in range(1,j+1)if len(q[i])<1][0].insert(0,q[j].pop(0))
                print(q)
            else:
                X=[i for i in range(1,j+1)if q[i].count(j)<1][0]
                print('X:',X)
                if set(q[X])=={*range(1,j)}:
                    g=q[X].pop(0)
                    print('g:',g)
                    q[[i for i in range(j,0,-1)if i!=X and q[i][0]>=g][0]].insert(0,g)
                    print('ok')
                else:
                    g=q[X].pop(0)
                    print('g:',g)
                    q[[i for i in range(1,j+1)if i!=X and q[i][0]>=g][0]].insert(0,g)
                print(q)
        elif q[j].count(j)==1:
            break
## J(3)

def J2(j):
    q={i:[i]*j for i in range(1,j+1)};print(q)
    while any(q[i]!=[*range(1,j+1)]for i in q.keys()):
        if any(len(q[i])<1 for i in range(1,j)):
            g=q[j].pop(0)
            print(g)
            q[[i for i in range(1,j)if len(q[i])<1][0]].insert(0,g)
        else:
            X=[i for i in range(1,j+1)if len(set(q[i]))==1and q[i][0]!=j][0]
            g=q[X].pop(0)
            print(g)
            q[[i for i in range(1,j+1)if i!=X and q[i][0]>=g][0]].insert(0,g)
        print(q)

J2(3)



