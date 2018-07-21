def d(*args):
	import itertools;u=[args[0+i:2+i]for i in range(0,len(args),2)];print(args);print(u);r=[l for l in itertools.combinations(u,2)];print(r);count=0
	for g in r:
		if g[0][::-1]==g[1]:
			count+=1
		elif g[0][0]<g[1][0]and g[0][1]>g[1][1]:
			count+=1
		elif g[0][0]>g[1][0]and g[0][1]<g[1][1]:
			count+=1
		else:
			pass
	print(count)

d(1,2,2,1)

##################################################
# CORRECT FOR ALL LARGE AND SMALL TEST CASES! :D #
##################################################

def d2():
    import re,itertools;from collections import defaultdict as dd;l=[];o=[];case=0
    with open('A-large-practice.in.txt','r')as e:
        e.readline();case=0
        q=''.join(e.readlines()).split('\n')
        for t in q:
            if re.match('^(\d*\s+)+[\d]*$',t):
                l.append(tuple([int(o)for o in t.split()]))
            else:
                o.append(t)
    y=[]
    for i in o[:len(o)-1:1]:
        y.append(l[:int(i):1])
        del l[:int(i):1]
    m=open('Output2.txt','w')
    for x in y:
        case+=1
        count=0
        r=[l for l in itertools.combinations(x,2)]
        for g in r:
                if g[0][::-1]==g[1]:
                        count+=1
                elif g[0][0]<g[1][0]and g[0][1]>g[1][1]:
                        count+=1
                elif g[0][0]>g[1][0]and g[0][1]<g[1][1]:
                        count+=1
                else:
                        pass
        m.write('Case #{}'.format(case)+': '+str(count)+'\n')
    m.close()

######################################################
# e and e2 are defined for Problem A. Counting sheep #
######################################################

def e():
    j=[];o=list(range(10));case=0
    with open('TestInput.txt','r')as e:
        e.readline()
        for r in e.read().split():
            count=0
            case+=1
            j.clear()
            while True:
                r=int(r)
                count+=1
                u=r*count
                if count>1 and u==r:
                    break
                for v in list(str(u)):
                    if int(v)in j:
                        pass
                    else:
                        j.append(int(v))
                if all(i in j for i in o):
                    break
            if count>1 and u==r:
                print('Case #{}'.format(case)+': '+'INSOMNIA')
            else:
                print('Case #{}'.format(case)+': '+str(u))
    
e()

def e2(r):
    j=[];count=0;o=list(range(10))
    while True:
        count+=1
        u=r*count
        if count>1 and u==r:
            break
        for v in list(str(u)):
            if int(v)in j:
                pass
            else:
                j.append(int(v))
        if all(i in j for i in o):
            break
    if count>1 and u==r:
        print('INSOMNIA')
    else:
        print(u)

e2(2)

########################################
# b is defined for Problem C. Coin Jam #
########################################
    
def b(j,n):
    import random;r=[]
    while 1:
        print('I')
        u='1'
        for i in range(n-2):
            u=u+str(random.randint(0,1))
        print(u)
        for i in range(2,11):
            print('`1st`: {}'.format(i))
            if any(int(u,i)%g==0 for g in range(2,int(u,i))):
                    print('`2nd`: {}'.format(i))
                    r.append(u)
                    break
            else:
                    continue
    print('hi')
    print(u)

def b2(N,J):
        import itertools;e=set(itertools.product("01", repeat=(N-2)));s=set();i=[];c=[];q=[];T=[];R=[];B=[]
        for v in e:
                s.add('1'+''.join(v)+'1')
        for g in s:
                c.append([int(g,e)for e in range(2,11)])
        print(len(c))
        for x in c:
##                print('`x`: {}'.format(x))
                for b in x:
##                        print('`b`: {}'.format(b))                                
                        i.append([b%a for a in range(2,101)])
                        T.append([a for a in range(2,101)if b%a==0])
##                        print('`T`: {}'.format(T))
##                        print('hi')
                for N in i:
                        R.append(any(m==0 for m in N))
##                print('`R`: {}'.format(R))
                i.clear()
                if all(Z for Z in R):
                        q.append(x[-1])
                        B.append([max(o) for o in T if len(o)>0])
##                        print('`B`: {}'.format(B))
                T.clear()
                R.clear()
        V=iter(q)
##        print(B)
        for _ in range(J):
                print(str(next(V))+': '+''.join(str(B[0])))
                del B[0]

##b2(32,500)

###################################################
# Judged Response for C-small Test Case: Correct! #
###################################################

def b3(N,J):
        import itertools;e=itertools.product("01", repeat=(N-2));s=set();c=[];q=[];T=[];B=[]
        for v in e:
                s.add('1'+''.join(v)+'1')
        for g in s:
                c.append([int(g,e)for e in range(2,11)])
##        print(len(c))
        for x in c:
##                print('`x`: {}'.format(x))
                for b in x:
##                        print('`b`: {}'.format(b))
                        T.append([a for a in range(2,1001)if b%a==0])
##                        print('`T`: {}'.format(T))
                if all(len(i)>0 for i in T):
                        q.append(x[-1])
                        B.append([min(i)for i in T])
                T.clear()
        V=iter(q)
##        print(B)
        F=open('NewOutput2.txt','w')
        F.write('Case #1:\n')
        for _ in range(J):
                F.write(str(next(V))+' '+' '.join([str(j)for j in B[0]])+'\n')
                del B[0]
        
##b3(16,50)

def crane(y):
        import re;p={1:1};count=1;u=1;v=re.findall('\(\w+\)',y);count2=0
##        print('v: ',v)
        for i in y:
##                print('`y`: {}'.format(y))
##                print('`i`: {}'.format(i))
                if i=='f':
                        if count==2**40:
                                count=1
                        else:
                                count+=1
                        if count not in p.keys():
                                p.update({count:1})
##                        print('`p`: {}'.format(p))
##                        print('`count`: {}'.format(count))
                        u=count
##                        print('`u`: {}'.format(u))
                        count2+=1
##                        print('`z`: {}'.format(z))
##                        print('`i2`: {}'.format(i))
                elif i=='b':
                        if count==1:
                                count=2**40
                        else:
                                count-=1
                        if count not in p.keys():
                                p.update({count:1})
                        u=count
                        count2+=1
##                        print('`u`: {}'.format(u))
##                        print('`z`: {}'.format(z))
                elif i=='u':
                        p[u]-=1
                        if p[u]==0:
                                p[u]=256
                elif i=='d':
                        p[u]+=1
                        if p[u]==257:
                                p[u]=1
##                        print('p: ',p)
                elif i=='(':
                        o=p[u]
                        j=count
                        while p[u]>2:
##                                print('hi!')
                                if p[u]==o and count>10:
                                        count2=count2+(v[0].count('f')*2**40)+(v[0].count('d')*2**40)
                                        count=count+((v[0].count('f')*2**40)-(v[0].count('d')*2**40))
                                        if count>=2**40:
                                                count=2**40-count
                                        elif count<2**40:
                                                count=2**40-count
                                        print(count)
                                        u=count
                                        p[u]=1
                                        break
                                m=(v[0])
##                                print('u,p[u]: ',u,p[u])
##                                print('m: ',m)
                                for g in m:
                                        if g=='f':
                                                if count==2**40:
                                                        count=1
                                                else:
                                                        count+=1
                                                if count not in p.keys():
                                                        p.update({count:1})
                                                u=count
                                                count2+=1
##                                                print('`z2`: {}'.format(z))
                                        elif g=='b':
                                                if count==1:
                                                        count=2**40
                                                else:
                                                        count-=1
                                                if count not in p.keys():
                                                        p.update({count:1})
##                                                print('`count2`: {}'.format(count))
                                                u=count
                                                count2+=1
##                                                print('`z3`: {}'.format(z))
                                        elif g=='u':
                                                p[u]-=1
                                                if p[u]==0:
                                                        p[u]=256
##                                                print('`p`: {}'.format(p))
                                        elif g=='d':
                                                p[u]+=1
                                                if p[u]==257:
                                                        p[u]=1
##                        print(p[u])
                        del v[0]
##                        print(y)
        return str(count2)

##print(crane('ufbbfffdubfdbffffuudbffdddfbfbfbfdffbffffffufbuufdfbffubbfffbfbddfbbfuubfbfdbdfuffffbfffufffudbudbdbffuufuffbbufuffuffbudbfdfdfbffbffffffdfdfffufubfubbbdfuffddduffufffbdffbbffuuffbffudfdbffubufbufdudfufffduffubddfdffffuuudbfffbbubdfffbbduddfuuffubbffffdfbuubfbfbudffuffdubfffdffffdbudffufdffffuubfffdufubddfufdufdfffffffbdbuubddbfuubffuffufffdfffbfffudffffdfufbubfdddbfdffudfbfbffbfufffdduffbbdfdffbffffbdfffffbffdfuffddffffuffbdfdudbfbubufbfdubfubdbbffbbbubduffbduffdddbbffbbdfufbufffffbfbufffffffufdbfffffdffbfbfuuffufbbffuffdfdffbfbuuufbfffdfufbffubffbffuudufdufduddudubdfffuffffuffffbfbffffffffbbfbfffffdffbfdffdfbubdbbbffffbffbuuffufbfbffdfdfdudbffbffbffffddbddfffdddbudfuuufuubfffdufbfufuffdfufuuffuufddbudfdbubbubfdbfufuffbdfbuffffufubdfuufdffbffffuuudffffdfbufdubdfufubbdffuduffdfbdffffdfuuffudfffuubfbdfffffufdfbdbfdffffffffufffufufbffdbdufudufffduuffffbdfddfffbuufdbfdufdffffbfbdfdfudffffbufu(bubbdbubdubbbfbdfbbbbdbbbbbbuuufubuubbfubbbubdbdbbbubufbbbbfbbbbfbdffbbdbbbbbbbbbbddbbbubbdbbubbuububbbbbfbbbuubufdbbububddbbfdbfuubbbbuffdbbbddubbfudbbfbfudfbbbbbbdbuuubdubbfbubbbbbbbuu)ddubdbdbbubfbdbbfubbuudufbubbdbubudbbbbdbddfbbbuddbdbdbbdbubfbbbbbbuubbbbbudbddddbbdudfbfddbbdudfdbfbbbdddbdbubffdubfbbbbbbbbddbddbbudduubbbfbbbbuududbbbfubbdfbdubufdbbbfdfbuddfbudfffbfbdbbbbbbbfduufdbfbfbbbfddfdbbbbbfdbbbubububduubddbbffbdbbbbubfdbbuububfuffbuubbbbbbbffbbbdubdbbdbddbdbbfbdfbbbbfbbfbbfbbdbbbufdbffdbffbbfbubbfdbuufudbbbbbbuudbdfbbdfbbdbfdbbbbbbbbdffububfbbbbfbbbbbdufdbubbbdfbfbbbbdbbuddbfubfbbbbdbbffbfdbbbbbfbbfbfufuubbubdbbdbbbbfbfbbbbubbbdbdbdufbubddbdffbbubbbbbddbfbubbbudfudubfbddbubbddbdfububfbbffbdbfbdfdbubdbbbffbbddbbfudbffbdbbbfudfbdddbbbdbbbbuufbbbbufbbdbbbbbbubbfdbbuffbbbbbubbbbubbfbbbbfbbbbbbbfbubbfubbubfufdbbbdbdbbudbufbuuduuubdbfbffbdfbfbbdfbbbbbdfbfbduuufbfffbuuuuuubdfbbbbbbufdbbdbubbbbbubudbfbbdbuubfbbdbubbufbbuuubbbddffbbbfbddbbbuubbfbufbfbbdbfbfuuubdu'))
##print(crane('ufbbfffdubfdbffffuudbffdddfbfbfbfdffbffffffufbuufdfbffubbfffbfbddfbbfuubfbfdbdfuffffbfffufffudbudbdbffuufuffbbufuffuffbudbfdfdfbffbffffffdfdfffufubfubbbdfuffddduffufffbdffbbffuuffbffudfdbffubufbufdudfufffduffubddfdffffuuudbfffbbubdfffbbduddfuuffubbffffdfbuubfbfbudffuffdubfffdffffdbudffufdffffuubfffdufubddfufdufdfffffffbdbuubddbfuubffuffufffdfffbfffudffffdfufbubfdddbfdffudfbfbffbfufffdduffbbdfdffbffffbdfffffbffdfuffddffffuffbdfdudbfbubufbfdubfubdbbffbbbubduffbduffdddbbffbbdfufbufffffbfbufffffffufdbfffffdffbfbfuuffufbbffuffdfdffbfbuuufbfffdfufbffubffbffuudufdufduddudubdfffuffffuffffbfbffffffffbbfbfffffdffbfdffdfbubdbbbffffbffbuuffufbfbffdfdfdudbffbffbffffddbddfffdddbudfuuufuubfffdufbfufuffdfufuuffuufddbudfdbubbubfdbfufuffbdfbuffffufubdfuufdffbffffuuudffffdfbufdubdfufubbdffuduffdfbdffffdfuuffudfffuubfbdfffffufdfbdbfdffffffffufffufufbffdbdufudufffduuffffbdfddfffbuufdbfdufdffffbfbdfdfudffffbufu(bubbdbubdubbbfbdfbbbbdbbbbbbuuufubuubbfubbbubdbdbbbubufbbbbfbbbbfbdffbbdbbbbbbbbbbddbbbubbdbbubbuububbbbbfbbbuubufdbbububddbbfdbfuubbbbuffdbbbddubbfudbbfbfudfbbbbbbdbuuubdubbfbubbbbbbbuu)ddubdbdbbubfbdbbfubbuudufbubbdbubudbbbbdbddfbbbuddbdbdbbdbubfbbbbbbuubbbbbudbddddbbdudfbfddbbdudfdbfbbbdddbdbubffdubfbbbbbbbbddbddbbudduubbbfbbbbuududbbbfubbdfbdubufdbbbfdfbuddfbudfffbfbdbbbbbbbfduufdbfbfbbbfddfdbbbbbfdbbbubububduubddbbffbdbbbbubfdbbuububfuffbuubbbbbbbffbbbdubdbbdbddbdbbfbdfbbbbfbbfbbfbbdbbbufdbffdbffbbfbubbfdbuufudbbbbbbuudbdfbbdfbbdbfdbbbbbbbbdffububfbbbbfbbbbbdufdbubbbdfbfbbbbdbbuddbfubfbbbbdbbffbfdbbbbbfbbfbfufuubbubdbbdbbbbfbfbbbbubbbdbdbdufbubddbdffbbubbbbbddbfbubbbudfudubfbddbubbddbdfububfbbffbdbfbdfdbubdbbbffbbddbbfudbffbdbbbfudfbdddbbbdbbbbuufbbbbufbbdbbbbbbubbfdbbuffbbbbbubbbbubbfbbbbfbbbbbbbfbubbfubbubfufdbbbdbdbbudbufbuuduuubdbfbffbdfbfbbdfbbbbbdfbfbduuufbfffbuuuuuubdfbbbbbbufdbbdbubbbbbubudbfbbdbuubfbbdbubbufbbuuubbbddffbbbfbddbbbuubbfbufbfbbdbfbfuuubdu'))
##print(crane('dddd(fdddddbu)f(fdddddbu)'))
##print(crane('uuufffuffffbfuffubffdfuuuffbfffbufbdfbdfffffdfufuubbfbudfdfduffffdduffduu(ffudfuudbfffbffbdffbbffffffdbudfbudfudfuufudffffbfddffdfddffdbufdufubfbfdfudbffbdfdffuffffffddubdbddbfbdbfubfbdffbbfdfuufdffuffufdbfbbbfffufffffffffbbfbdfddufffduudubfbfdfffubffbfufffudufbfdffubufffdfddffffbbffdbffdfbfffbbffffbuffffubfffbfffdfdffffudffffdffufbbdufffdffdffufuudffffffbffffbdffuffffbfffffufbbfufbbbffbudffbuubfdfbfdffdffbbufbufffffbuffbffbbbbbfufuufffffdfdfffudffbffdubuufffdfdffuuuffuffdfudbffbbffdffffbdudfdffbuudfdfdbffbffdbffffudffbdfdfuffffbufffbduuuffdffffuduffuufufffubbuffudffbufuufuubfuffuddfbfdfffbdufffffddfffbubfffffubudfffbdfdfffffbbfffffffdbudffbfffdffffbffbfuuddffdffbfbufdfbddfffbffufdufubffuffdbffbfffdufffdffffufdfffffffbbuuubbfdfbdbbduubbfufbduffffffdbdffbbfdubdffbdfdufbfdfffffbbfffbdfddbfuffbuuffdfdffdbbuuffdbfuffdbfddfufbfbfubdfufdfufffffuuffudfuffffufdffufddfffffffffbddffdffdffbfdfffbffdbdfdbdbfdfdfuffubdbbdfbbffuudfubffffffdfffuuffddfubffbdfbbufufffffbfbuddffduffuffdubdffffffbdbdfffbbbududffufffudfffffffffbdubffufudffdffubddufbfdffdbbubuffdbfddfdfufdfdfffbfubfufffbfuuuffudbuffdfbffdubffuffbbufffdbffddufdffuuuu)bbubbfudbbubdbdbfubbbbudfbdfbfbbfbbfbdbdbbbbbbbbbbbbubdbbdbbbbbbbbfubbfuufbuuuffuubbufuubufubdbbddbbudfbfdbbddfbbbbdfdfbddbddfudufbbufbbbbbddbfbbbfbudbdudfdbdfdfudbubbbdbbbbbbbbbdbfdbubbudfubdubbfbfbuubdfbbdfbfdfduddbbbubbbdbbubfbbfbbbbdbbubfufuubbfbbbfbdddubddubbbbbfbbudbbbfbfufdubbfbdbufbbdbddubdbufdddfbdufdufbbbbbbbbbbufbbbbdubbfbbfubbdfufbdubdddubbuuubbdfbbbbubfudbuubfbubbbbbufudbbbdduubbudffufubfuffbbdbubdbdubudbddbduubfbfduufdbdfbubfbbbdbbbbfufdbubfbubbbbddbufbbuffdbdbbubfdbbbufubbbububfbbbbubfbfbuububbbdufbbfudbbbdduufubbbbudbbbufbbddbbfbbdbuudubbdfubfbfbbubbbbbddbubbbbffudbdufdbduufbbbffbbbuudubbbdfdubbfbbufffuddffbbfuufbufdbbubbbbdudbbffbbbbbfbbbbddbubbbdbbffbbubfu'))
##print(crane('bbbbbbdfdddbbbbbbffbdbbfbbbudubbdubbufbfdbbbbufuuddbubdbbudbbudfufbbdbfdbbbbddfuufbbfbddbbduubbuuubffdbdbbdbbbbubbfdddubbubbbfbuudbbfbubfudfbbfbufbbfbbbfdfbfffdbbbbubbdubbbbfbdudfbbdbbubbdfddbdfbbbfbudbbdubbbfbfbbudfdduufbbbbubbbfubuduuubbfufbbdbbbbfbbbubdbbdbfdfbdffbbbbbdfbbbudbbbdffbdubbbufbfbbuudbbfbbfdbbfddbffbubububfbbffubdbffbbfbbbuubbdbdubfbbubufbbbddbbbbbfbbfbbbbufbdbdbdbudfufbubbfbfdbdbdbfdbduubdudfbudbbbudbbbububbuddbbfbbbbudubdbfbuubbbuubudbubddudbfbuubdffbbbbfbbbbubbfbubbbuufubdbubbbdbdbbbubfbbbu(bbdbbfffudbbbbbudfdubbbfbbbuuudbdbbbbudbbfuuubbbudffdbbdfffdfddbdffdbfdbbbbbdububddbbuffbfdbbubdbufdfdbudbbbdbbbbbufbubbbbbbbbbbbfbbfffdbdbbufuddfbbbufuubbbddufufdbbdddbbuufbubfffubbfuubdfbfbddbdbbfbbbfububbbbbbdbbfbubbdbbbdfbfbubbbbuduububbbbbfbuuubbfffffbbbfbbffbbdbbbdbfbbbubbbffbbdbfbubbbbfbuubbdbdbbbfbbbdbbbubdbbbdbbdbubdudbfbbbdbbffuddbdbubbbbbfbfdubbdbbudfuubdfbbfbububuubfbbbubbubbbbbfuubbbbbubbdufbddffddfbdduubububfdfbufbbfbbffdubbddubfuuddbbfbbbbbfbuffbbfudbduduffufbbbfbbbbdffbbbdbfbdbubdddbbddbbbbdbbfbbudbudfbuubbfbfbbduudbbfuuufbfdbbbdubdbuudfbdffubdfbbbubdufbdbubbdbbdbdbbfbfffbubdbbfbbbufbbubbdudbduubbfbdbbdfbbubbddudbufddduubbbfbbddduubufdbbffbbdfbdbbfbdfudddbfdffufudbubbudfbbubfbbbffbdbbdudbbdbfbbbbbbdubbubufbbubdbddbbbbbfbdbbddbfdbbbbbddfbbbduubbdfuubbbbffbbuubdfubdddbubdububbfbfubbbbdbbbbbdbbfbubbfbudbbbufbddbuubdfbfbbdbddbfbfbfbbbffbfbfbdbbbdbdbubububbdbbdbbbbdbbbubuubfbubfddbfubbbbbdbbufubufbdbbbbdddbubbfbfububbbbbbbdfbubbbbfbbbbbfdubbbdfbbduududdffbbbdbfbfbbbbfbfdfbdbfbuufubdubbubbdbbbbbfdbubfddbdbdbbbbbubbbbufbfduubbbbbduubdubbbbdbfubfdfdbfbbbubbbbfdbbfdbfbbbfdbuuudbdbbbbufbbubbdfbuububbdbubbdbbuufubbubbbbbfbbubfffbfbfdbbbbbububbbbudbduubbubdbbuuffudfbddbbddbdubdubfbdbdbdbbbubufffbuubffbbu)dbbudbbbbdbbudubbdbudfdubbdffdbubfbubuffdubfbbbfuubbubbbbbbfubbbbbuddudbbdubdfbudbfbdbffbdddbbdfddbbbfbfdfbbbbffudffbdudbbffbdbbubbbdufubdbdfdddbububbbbbudfububbudffffbbbbfububbdfdbbbubbbdfbdubbdbubfdudbdfbfbbbfubddbbbbbddfdbbfbfdbdubdbffbbdbbbfbbubbbbfbbbuu'))
case_no=0
g=open('F-small-practice.in.txt','r')
print('{} total test cases'.format(''.join(g.readline().split())))
t=open('CraneTruckOutput.txt','w')
for e in g.readlines():
        print(str(case_no)+'\n'+str(e))
        case_no+=1
        t.write('Case #{}: '.format(str(case_no))+str(crane(''.join(e.split())))+'\n')
t.close()
                                
                        
