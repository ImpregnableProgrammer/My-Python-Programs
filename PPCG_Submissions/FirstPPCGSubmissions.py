

###################
#### FIRST ONE ####
###################

################
# Test version #
################

def Interview2(h):
    print(h)
    print(h[0:int(len(h)/2.71828)-1])
    k = max(h[0:int(len(h)/2.71828)-1])
    print(k)
    n = max(h[int(len(h)/2.71828)-1:len(h)-1])
    return max([k, n])

h = [1,2,3,4,5,6]

print(Interview2(h))

#####################
# Code-Golf Version #
#####################

def Interview(h):k=max(h[0:int(len(h)/2.71828)-1]);n=max(h[int(len(h)/2.71828)-1:len(h)-1]);return max([k, n])

####################
#### SECOND ONE ####
####################
from collections import OrderedDict
print('\rSECOND ONE:\r ')
################
# Test Version #
################

h = {'0': list('qwertyuiop'), '1': list('asdfghjkl'), '2': list('zxcvbn')}
print(h.keys())
n = [['qwertyuiop'], ['asdfghjkl'], ['zxcvbnm']]

l = [list('qwerty'), list('hello')]

if set(l[0]).issubset(set(h['0'])):
    print('hi')
else:
    print(l[0], h['0'])
    print('Nope')
    
n = [''.join(j) for j in l if set(j).issubset(set(h['0'])) or set(j).issubset(set(h['1'])) or set(j).issubset(set(h['2']))]

##for i in l:
##    print(i)
##    y = [(i.lower()).issubset(k) for k in h.keys()]
##    print(y)
    

###################
#### THIRD ONE ####
###################

print('\rTHIRD ONE:\r ')

################
# Test Version #
################

def d(a, b):
    o=[];o+=([str(bin(g)).lstrip('0b')if str(type(g))=="<class 'int'>"else str(bin(ord(g))).lstrip('0b')for g in a]);n=[''.join(o)[i:i+b]for i in range(0,len(''.join(o)),b)];v=[]
    for t in n:
        if len(t)!=b:n[n.index(t)]=str(t)+'0'*(b-len(t))
    v+=([int(str(f),2)for f in n])
    return v

## print(d("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel est eu velit lacinia iaculis. Nulla facilisi. Mauris vitae elit sapien. Nullam odio nulla, laoreet at lorem eu, elementum ultricies libero. Praesent orci elit, sodales consectetur magna eget, pulvinar eleifend mi. Ut euismod leo ut tortor ultrices blandit. Praesent dapibus tincidunt velit vitae viverra. Nam posuere dui quis ipsum iaculis, quis tristique nisl tincidunt. Aliquam ac ligula a diam congue tempus sit amet quis nisl. Nam lacinia ante vitae leo efficitur, eu tincidunt metus condimentum. Cras euismod quis quam vitae imperdiet. Ut at est turpis.", 16))

print(d('Hello World', 50))
    
print(len('''def d(a, b):
o=[];o+=([str(bin(g)).lstrip('0b')if str(type(g))=="<class 'int'>"else str(bin(ord(g))).lstrip('0b')for g in a]);n=[''.join(o)[i:i+b]for i in range(0,len(''.join(o)),b)];v=[]
for t in n:
    if len(t)!=b:n[n.index(t)]=str(t)+'0'*(b-len(t))
v+=([int(str(f),2)for f in n])
return v'''))

##def d2(a, b):
##    o=[];o.append([str(bin(g)).lstrip('0b')if str(type(g))=="<class 'int'>"else str(bin(ord(g))).lstrip('0b')for g in a]);n=[''.join(o[0])[i:i+b]for i in range(0,len(''.join(o[0])),b)];
##    for t in n:
##        if len(t)!=b:z=n.index(t);n[z]=str(t)+'0'*(b-len(t));v=[];v.append([int(str(f), 2)for f in n]);
##    return v[0]
##
##print(d2([1,2,3,4,5], 1))

print('\rTHIRD ONE:\r')
g=lambda h:tuple(''.join(sorted([f.strip('(').strip(')') for f in''.join(str(h).strip('(').strip(')'))if f in [str(i)for i in range(10)]])))

y = (1,2,(3,4),(5,6,(8,7)), (5,6))

print(g(y))

print('\rCOUNT:\r')
print(len("g = lambda h: tuple(''.join(sorted([f.strip('(').strip(')') for f in ''.join(str(h).strip('(').strip(')')) if f in num])))"))

print('\rFOURTH ONE:\R:')
from random import*;lambda a,c:sample(range(1,c+1),a)

print('\rFIFTH ONE:\r')

##def q(a):
##    for l in [('_'*25+'.')*z for z in range(a+1)][-1].split('.'):
##        n=list(l);n.insert(randrange(len(n)+1),' '*5);
##        if n.count(' '*5)!=1:
##            for o, h in enumerate(n):n[o]=' 'if o==5-n.count(' ')else h
##        print(''.join(n)+'\r')

##print(len('''def q(a):
##    for l in list([('_'*25+'\r')*z for z in range(a+1)][-1].split('\r')):
##        n=list(l);n.insert(randrange(len(list(l))+1),' '*5);
##        if list(n).count(' '*5)!=1:
##            for o, h in enumerate(n):
##                if o==5-n.count(' '):n[o]=' '
##        print(''.join(n)+'\r')'''))
##
##print(len('''def q(a):
##    for l in list([('_'*25+'\r')*z for z in range(a+1)][-1].split('\r')):
##        n=list(l);n.insert(randrange(len(n)+1),' '*5);
##        if n.count(' '*5)!=1:
##            for o, h in enumerate(n):n[o]=' 'if o==5-n.count(' ')else h
##        print(''.join(n)+'\r')'''))

##q(12)

##n=[]
##f = lambda a, : [list(l)for l in list([('_'*25+'\r')*z for z in range(a+1)][-1].split('\r'))].insert(randrange(len(list(l))+1), ' '*5));print(n)
##f(5,n)

##j=('_'*25+' '*5)
##n = random.randrange(len(j)+1)
##print(j)
##print('\rSIXTH ONE:\r')
##g=lambda a:print((j[-n:]+j[:-n]+'\r')*(a+1))

#######################
# Golfed Form & tests #
#######################

def g(a,j='_'*25+' '*5):
 for l in range(a):import random;n=random.randrange(len(j)+1);print(j[-n:]+j[:-n]+'\r'*4)

g(10)

print(len('''def g(a,j='_'*25+' '*5):
 for l in range(a):import random;n=random.randrange(len(j)+1);print(j[-n:]+j[:-n]+'\r'*4)'''))

############
# Ungolfed #
############

def g2(a,j='_'*25+' '*5):
    import random
    for l in range(a+1):
        n=random.randrange(len(j)+1)
        print(j[-n:]+j[:-n])      


print('\rSIXTH ONE:\r')

zl = [chr(i+65)for i in range(26)]
print(zl)

print("-"*25+'''
|       |  ABC  |  DEF  |
|   1   |   2   |   3   |
'''+"-"*25+'''
|  GHI  |  JKL  |  MNO  |
|   4   |   5   |   6   |
'''+"-"*25+'''
| PQRS  |  TUV  | WXYZ  |
|   7   |   8   |   9   |
'''+"-"*25+'''
|       |       |       |
|   *   |   0   |   #   |
'''+"-"*25)

print(len("""_"*25+'''
|       |  ABC  |  DEF  |
|   1   |   2   |   3   |
'''+"-"*25+'''
|  GHI  |  JKL  |  MNO  |
|   4   |   5   |   6   |
'''+"-"*25+'''
| PQRS  |  TUV  | WXYZ  |
|   7   |   8   |   9   |
'''+"-"*25+'''
|       |       |       |
|   *   |   0   |   #   |
'''+"-"*25)"""))
##v='\n'+'-'*25+'\n';print(v+'|'+' '*7+'|  ABC  |  DEF  |\n|   1   |   2   |   3   |'+v+'|  GHI  |  JKL  |  MNO  |\n|   4   |   5   |   6   |'+v+'|  PQRS |  TUV  |  WXYZ |\n|   7   |   8   |   9   |'+v+'|       |       |       |\n|   *   |   0   |   #   |'+v)

##h=open('/Users/Rohan/Google Drive/Phone.txt','r').read();print(h)
##print(len("""v='\n'+'-'*25+'\n';print(v+'|'+' '*7+'|  ABC  |  DEF  |\n|   1   |   2   |   3   |'+v+'|  GHI  |  JKL  |  MNO  |\n|   4   |   5   |   6   |'+v+'|  PQRS |  TUV  |  WXYZ |\n|   7   |   8   |   9   |'+v+'|       |       |       |\n|   *   |   0   |   #   |'+v)"""))

##u=['\n'+'-'*25,'\n|',[],'|',[],'|','\n|',[],'|',[],'|\n','\n'+'-'*25,'\n|',[],'|',[],'|','\n|',[],'|',[],'|','\n'+'-'*25


n="-"*25+'\n'
q=' '*3
zn = [q,'ABC','DEF',' 1 ',' 2 ',' 3 ','GHI','JKL','MNO',' 4 ',' 5 ',' 6 ','PQRS','TUV','WXYZ',' 7 ',' 8 ',' 9 ',q,q,q,' * ',' 0 ',' # ']
for i in range(int(len(zn)/3)):
 if i%2==0:
  if len(zn[:3:1][0])==4:print(n+'|  {} |  {}  |  {} |'.format(*zn[:3:1]))
  else:print(n+'|  {}  |  {}  |  {}  |'.format(*zn[:3:1]))
 else:print('|  {}  |  {}  |  {}  |'.format(*zn[:3:1]))
 del zn[:3:1]
print(n)

k=' ABC DEF 1 2 3 GHI JKL MNO 4 5 6 PQRS TUV WXYZ 7 8 9    * 0 #'.split(' ')
for _ in range(8):
 print('\n',end='')
 if _%2==0:print("-"*27+'\n',end='')
 [print('|{}|'.format(g.center(7)),end='')for g in k[:3:1]];del k[:3:1]
print('\n'+"-"*27)

print(len("""k=' ABC DEF 1 2 3 GHI JKL MNO 4 5 6 PQRS TUV WXYZ 7 8 9    * 0 #'.split(' ')
for _ in range(8):
 print('\n',end='')
 if _%2==0:print("-"*27+'\n',end='')
 [print('|{}|'.format(g.center(7)),end='')for g in k[:3:1]];del k[:3:1]
print('\n'+"-"*27)"""))

##print((n+l+l)*3)
##def a(v):
## j=[chr(i+65)for i in range(3)];n=['\n'+'A|_|','\n'+'B|__|', '_\n'+'C|___|'];op=od((item,[])for item in j)
## for l in op:op[l]=n[0];del n[0]
## if v in range(1,27):print('  _'+str((op['A']+op['B']+op['A'])+op[v])*int(v))
##
##print(len("""from collections import OrderedDict as od
##def a(v):
## n=['\n'+'A|_|','\n'+'B|__|', '_\n'+'C|___|'];op=od((item,[])for item in [chr(i+65)for i in range(3)])
## for l in op:op[l]=n[0];del n[0]
## if v in range(1,27):print('  _'+str(op['A']+op['B']+op['A']+op['C'])*int(v))"""))
##
##a(20)

##def a(v):
## ##n=['\n'+'A|_|','\n'+'B|__|', '_\n'+'C|___|'];op=od((item,[])for item in [chr(i+65)for i in range(26)])
## j=[chr(i+65)for i in range(26)]
#### n=list(range(1,27))
#### op=od((item,[]) for item in j)
#### for l in op:op[l]=n[0];del n[0]
## d=od((j[i], ('  '+'_'*(i+1)+'\n'+j[i]+'|'+'_'*(i+1)+'|')) for i in range(26))
## f=lambda w:"a"[w:]or f(w-1)+chr(65+w)+f(w-1)
## l=f(v)
## for g in str(l).upper():
##     print(d[g])

##a(0)
 
##def a2(v):
##    n=list(range(1,27))
##    op=od((item,[]) for item in n)
##    j=[chr(i+65)for i in range(26)]
##    for l in op:op[l]=j[0];del j[0]
##    d=od((i, ('_'*(i-2)+'\n'+op[i]+'|'+'_'*i+'|')) for i in range(1,27));
##    n=f(v)
##    a(n)
##
##a2(10)

print('\rSEVENTH ONE:\r')

#################################
# Golfed Version and Execution: #
#################################

from collections import*
def a(v):o=OrderedDict;j=[chr(i+97)for i in range(26)];d=o((j[i],('  '+'_'*(i+1)+'\n'+j[i]+'|'+'_'*(i+1)+'|'))for i in range(26));f=lambda w:'a'[w:]or f(w-1)+j[w]+f(w-1);[print(d[g])for g in f(v)]

a(1)

print(len("""from collections import*
def a(v):o=OrderedDict;j=[chr(i+97)for i in range(26)];d=o((j[i],('  '+'_'*(i+1)+'\n'+j[i]+'|'+'_'*(i+1)+'|'))for i in range(26));f=lambda w:'a'[w:]or f(w-1)+j[w]+f(w-1);[print(d[g])for g in f(v)]"""))

#####################
# Ungolfed Version: #
#####################

print('\rANOTHER ONE:\r')
from collections import*
def a2(v):
    o=OrderedDict
    j=[chr(i+97)for i in range(26)]
    d=o((j[i],('  '+'_'*(i+1)+'\n'+j[i]+'|'+'_'*(i+1)+'|'))for i in range(26))
    f=lambda w:'a'[w:]or f(w-1)+j[w]+f(w-1)
    [print(d[g])for g in f(v)]

a2(1)

print('\rANOTHER ONE 2:\r')

def ins(a,v=None):
    z=sorted(list(a))
    if v:[print(z[i:i+v])for i in range(0,len(z),v)]
    else:print(z)


def r(n):
    print(g)
    print(len(set.intersection(set(*n))))
    

##r([[(-8,6),(-4,-2)],[(-4,9),(4,3)],[(2,10),(14,4)],[(1,7),(10,-6)],[(7,4),(10,2)],[(5,2),(9,-4)],[(-6,-4),(-2,-6)]])


print('\rTANK GAME: \r')

from math import*
def x(a,b):
    f={'Red':{'Health':10},'Blue':b}
    print(f['Red']['Health'])
    
    

##x((2,3,4,5),(2,3,4,5))

from random import*
m=lambda y:''.join(choice([q.upper(),q.lower()])for q in sorted(y.replace(' ','_'),key=str.isdigit))

##from random import*
##def sa():return''.join(choice([q.upper(),q.lower()])for q in sorted(input().replace(' ','_'),key=str.isdigit))
##
##sa()

print(m('hello'))

print(len("""from random import*
def sa():''.join(choice([q.upper(),q.lower()])for q in sorted(input().replace(' ','_'),key=str.isdigit))"""))

print(len("""from random import*
lambda y:''.join(choice([q.upper(),q.lower()])for q in sorted(y.replace(' ','_'),key=str.isdigit))"""))

print(m('hel232 lo'))

n=lambda i: print(''.join(choice([q.upper(),q.lower()])for q in sorted(i.replace(' ','_'),key=str.isnumeric)))

print(len("lambda i: print(''.join(choice([q.upper(),q.lower()])for q in sorted(i.replace(' ','_'),key=str.isnumeric)))"))

n('he2l4 l5o')

##az=lambda d,o=: [f() for f in 

##az('hello')

##def sa2(so):
##    v=[]
##    for a in so:
##        f=choice([a.upper,a.lower])
##        v.append(f())
##    ''.join(v).replace(' ','_')
##    print(''.join(v))


###################
# Golfed Version: #
###################

from re import*
def wq(r):
 a=sub('[+](?![0-9])','+1',sub('[-](?![0-9])','-1',r));q=lambda x:(not x.isdigit(),''.join(filter(str.isalpha,x)))
 for z in findall('(?<![0-9])[a-z]',a):a=a.replace(z,('+1{}'.format(z)))
 if not str(sorted(((sub('[.]','',sub('[+-]',' ',a))).split(' ')),key=q)[0]).isdigit():a+='+0, '
 for i in list(set(findall('[a-z]',a))^{'i','j','k'}):a+='+0{}, '.format(i)
 print(findall('[-]?\d+(?:\.\d+)?',''.join(sorted(sub('(?<=[A-Za-z0-9])(?=[+-])',', ',a).split(' '),key=q))))

wq('1-0k')

print(len("""from re import*
def wq(r):
 a=sub('[+](?![0-9])','+1',sub('[-](?![0-9])','-1',r));q=lambda x:(not x.isdigit(),''.join(filter(str.isalpha,x)))
 for z in findall('(?<![0-9])[a-z]',a):a=a.replace(z,('+1{}'.format(z)))
 if not str(sorted(((sub('[.]','',sub('[+-]',' ',a))).split(' ')),key=q)[0]).isdigit():a+='+0, '
 for i in list(set(findall('[a-z]',a))^{'i','j','k'}):a+='+0{}, '.format(i)
 print(findall('[-]?\d+(?:\.\d+)?',''.join(sorted(sub('(?<=[A-Za-z0-9])(?=[+-])',', ',a).split(' '),key=q))))"""))

# Test Case 1: WORKS!
# Test Case 2: WORKS!
# Test Case 3: WORKS!
# Test Case 4: WORKS!
# Test Case 5: WORKS!
# Test Case 6: WORKS!
# Test Case 7: WORKS!
# Test Case 8: WORKS!
# Test Case 9: WORKS!
# Test Case 10: WORKS!
# Test Case 11: WORKS!
# Test Case 12: WORKS!
# Test Case 13: WORKS!
# Test Case 14: WORKS!
# Test Case 15: WORKS!
# Test Case 16: WORKS!
# Test Case 17: WORKS!
# Test Case 18: WORKS!
# Test Case 19: WORKS!
# Test Case 20: WORKS!
# Test Case 21: WORKS!
# Test Case 22: WORKS!
# Test Case 23: WORKS!
# Test Case 24: WORKS!

#####################
# Ungolfed Version: #
#####################

from re import*
def wq2(r):
    # Substitute all minus (-) and plus (+) signs NOT followed by a number  (if there are any) with a "1"
    a=sub('[+](?![0-9])','+1',sub('[-](?![0-9])','-1',r))
    # Lambda function created for later use to sort the Quaternion. This function, when given as a key to the "sorted" function, arranges the input Quaternion in the order where the whole number comes first, and then the rest are placed in order of increasing letter value (i,j,k in this case) 
    q=lambda x:(not x.isdigit(),''.join(filter(str.isalpha,x)))
    # The following "for" loop replaces the letters NOT preceded by a number with a one followed by that letter
    for z in findall('(?<![0-9])[a-z]',a):
        a=a.replace(z,('+1{}'.format(z)))
    # The following first substitutes all pluses and minuses (+ and -) with a space, and then that new string is split at those spaces, and returned as a list. After that, the list is sorted according the the "lambda" function shown above. Then, the first item in that list, which is supposed to be a lone number, is checked to make sure that it indeed is a lone number. If it isn't, then "+0, " is appended to the Quaternion. 
    if not str(sorted(((sub('[.]','',sub('[+-]',' ',a))).split(' ')),key=q)[0]).isdigit():
        a+='+0, '
    # The following "for" loop finds ALL the letters NOT in the list, my finding the symmetric difference between a set of all the letters found, and a set containing all the letters needed. For the letters not in the list, a '+0' is added the quaternion, followed by that letter, and then a comma and a space.
    for i in list(set(findall('[a-z]',a))^{'i','j','k'}):
        a+='+0{}, '.format(i)
    # Finally, in this last step, a ", " is added IN BETWEEN unicode characters and pluses/minuses (+/-). Then, it splits at those spaces, and the commas separate different parts of the Quaternion from each other (otherwise, you would get something like `12i+3j+4k` from `1+2i+3j+4k`) in a returned list. Then, that list is sorted according to the lambda expression "q" (above), and then, finally, the NUMBERS (of any type, courtesy to Regex) are extracted from that joined list, and printed out in the correct order.
    print(findall('[-]?\d+(?:\.\d+)?',''.join(sorted(sub('(?<=[A-Za-z0-9])(?=[+-])',', ',a).split(' '),key=q))))


def rt(g):
 import re;y={1:'UI',2:'SI',3:'UD',4:'SD',5:'LE',6:'SY',7:'ST'}
 if g.isdigit():return y[1]
 elif bool(re.match('^[+-]\d+$',g)):return y[2]
 elif bool(re.match('^[0-9]\d*(\.\d+)?$',g)):return y[3]
 elif bool(re.match('[+-](?=[0-9]\d*(\.\d+))',g)):return y[4]
 elif bool(re.match('[a-zA-Z]+',g)):return y[5]
 elif bool(re.match('^[^A-Za-z0-9]+$',g)):return y[6]
 else:return y[7]

print(len("""def rt(g):
 import re;y={1:'UI',2:'SI',3:'UD',4:'SD',5:'LE',6:'SY',7:'ST'}
 if g.isdigit():return y[1]
 elif bool(re.match('^[+-]\d+$',g)):return y[2]
 elif bool(re.match('^[0-9]\d*(\.\d+)?$',g)):return y[3]
 elif bool(re.match('[+-](?=[0-9]\d*(\.\d+))',g)):return y[4]
 elif bool(re.match('[a-zA-Z]+',g)):return y[5]
 elif bool(re.match('^[^A-Za-z0-9]+$',g)):return y[6]
 else:return y[7]"""))

def rt2(g2):
 import re;y={'^\d+$':'UI','^[+-]\d+$':'SI','^[0-9]\d*(\.\d+)?$':'UD','[+-](?=[0-9]\d*(\.\d+))':'SD','[a-zA-Z]+':'LE','^[^A-Za-z0-9]+$':'SY'};d=[y[i]for i in list(y.keys())if re.match(i,g2)]
 if len(d)>0:return d[0]
 else:return'ST'
    
print(rt2('<>!-='))

print(len("""def r(g):
 import re;y={'^\d+$':'UI','^[+-]\d+$':'SI','^[0-9]\d*(\.\d+)?$':'UD','[+-](?=[0-9]\d*(\.\d+))':'SD','[a-zA-Z]+':'LE','^[^A-Za-z0-9]+$':'SY'};d=[y[i]for i in list(y.keys())if re.match(i,g)]
 if len(d)>0:return d[0]
 else:return'ST'"""))

def bv(ri):import itertools,re;r=[];[r.append(h)for h in itertools.permutations(re.sub("(?<=[a-zA-Z'])(?=[a-zA-Z])",' ',ri.replace('x','')).split(' '),2)if h[::-1]not in r and h not in r];return r

print(bv("WYxY'y"))

print(len("""def b(r):import itertools,re;r=[];[r.append(h)for h in itertools.permutations(re.sub("(?<=[a-zA-Z'])(?=[a-zA-Z])",' ',r.replace('x','')).split(' '),2)if h[::-1]not in r and h not in r];return r"""))

import re
q=lambda n:''.join([g[0].upper()for g in n.split()if g.upper()not in['OF','AND','BY','OR']])

###########################
# Longer, but using regex #
###########################

yre=lambda g:[(bin(len(f)),hex(len(f)),len(f))if int(f)>0 else ('0b0','0x0','0')for f in re.sub('(?<=\s)+\s','0 ',g).split()]

##############################
# Shorter, but without regex #
##############################

wer=lambda g:[(bin(len(f)),hex(len(f)),len(f))for f in g.split(" ")]


rmsd=lambda r,n:len({z for z in{v for f in{t for u in[[r-q**3,r+q**3]for q in range(1,n+1)]for t in u if any(t%g<1 for g in range(2,t))}for v in range(2,f)if f%v<1}if all(z%g>0 for g in range(2,z))})

print(rmsd(720,6))

print(len("lambda r,n:len({z for z in{v for f in{t for u in[[r-q**3,r+q**3]for q in range(1,n+1)]for t in u if any(t%g<1 for g in range(2,t))}for v in range(2,f)if f%v<1}if all(z%g>0 for g in range(2,z))})"))

##def d(r):
##	print('| |',end='')
##	y=[
##	for _ in range(len(r)):
##		[print('|{}|'.format(i),end='')for i in o[_]]
##	print('\n|0|',end='')
##	[print('|{}|'.format(u))for u in r if list(r).index(u)%16!=0 else print('\n|{}|'.format(o[(list(r).index(u))/16]))]
##	for _ in range(len(r)):
##
##[print('|{}|'.format(b),end='')if list(r).index(b)%16!=0 else print('\n|{}|'.format('0'),end='')for b in r]

def f(r):
 o=list(' 0123456789ABCDEF');print('+---'*17+'+');[print('| {} '.format(h),end='')for h in o];c,w=[],[];del o[0]
 for g in r:
  if len(c)%16<1:print('|\n'+'+---'*17+'+',end='');[print('\n| {} | {} '.format(j,g),end='')for j in o[0]];c.append(g);w.append(g);w.append(' ');del o[0]
  else:print('| {} '.format(g),end='');c.append(g);w.append(g)
 print('|\n'+'+---'*(len(''.join(w).split(' ')[-1])+2)+'+')

f('jvrvrbbjenbj;n;ekbn;gdosnbkjhvsdhvshksfnvksfbklf')

print(len("""def f(r):
 o=list(' 0123456789ABCDEF');print('+---'*17+'+');[print('| {} '.format(h),end='')for h in o];c=[];w=[];del o[0]
 for g in r:
  if len(c)%16<1:print('|'+'\n'+'+---'*17+'+',end='');[print('\n| {} | {} '.format(j,g),end='')for j in o[0]];c.append(g);w.append(g);w.append(' ');del o[0]
  else:print('| {} '.format(g),end='');c.append(g);w.append(g)
 print('|\n'+'+---'*(len(''.join(w).split(' ')[-1])+2)+'+')"""))

def f2(r):o=' 0123456789ABCDEF';r=[r[0+i:16+i]for i in range(0,len(r),16)];print('+---'*17+'+\n|',end='');[print(' {} |'.format(h),end='')for h in o];print(''.join([str(e+' | ')if e.isdigit()or e.isalpha()else str(e)for e in''.join([str('\n'+'+---'*17+'+\n| '+x[0]+x[1])for x in zip(o[1::1],r)])]));print('+---'*(len(r[-1])+1)+'+')

f2('ggreuuobgugoubgoubguorgoruguor')

print(len("def f(r):o=' 0123456789ABCDEF';r=[r[0+i:16+i]for i in range(0,len(r),16)];print('+---'*17+'+\n|',end='');[print(' {} |'.format(h),end='')for h in o];print(''.join([str(e+' | ')if e.isdigit()or e.isalpha()else str(e)for e in''.join([str('\n'+'+---'*17+'+\n| '+x[0])+x[1]for x in zip(o[1::1],r)])]);print('+---'*(len(r[-1])+1)+'+')"))
##print('+---'*17+'+');[print('| {} '.format(h),end='')for h in o]
##[print('| {} |'.format(x))for x in ''.join(e)]
## for g in r:
##  if len(c)%16<1:print('|\n'+'+---'*17+'+',end='');[print('\n| {} | {} '.format(j,g),end='')for j in o[0]];c.append(g);w.append(g);w.append(' ');del o[0]
##  else:print('| {} '.format(g),end='');c.append(g);w.append(g)
## print('|\n'+'+---'*(len(''.join(w).split(' ')[-1])+2)+'+')

def f3(r):o=' 0123456789ABCDEF';r=[r[0+i:16+i]for i in range(0,len(r),16)];print('+---'*17+'+\n|',end='');[print(' {} |'.format(h),end='')for h in o];print(''.join([str(e+' | ')if e.isdigit()or e.isalpha()else str(e)for e in''.join([str('\n'+'+---'*17+'+\n| '+x[0]+x[1])for x in zip(o[1::1],r)])]),end='');print('  |'+'   |'*(15-len(r[-1]))+'\n'+'+---'*17+'+')

f3('hi')

print(len("def f3(r):o=' 0123456789ABCDEF';r=[r[0+i:16+i]for i in range(0,len(r),16)];print('+---'*17+'+\n|',end='');[print(' {} |'.format(h),end='')for h in o];print(''.join([str(e+' | ')if e.isdigit()or e.isalpha()else str(e)for e in''.join([str('\n'+'+---'*17+'+\n| '+x[0]+x[1])for x in zip(o[1::1],r)])]),end='');print('  |'+'   |'*(15-len(r[-1]))+'\n'+'+---'*17+'+')"))

import time
def r(r,k):
 print(time.ctime())
 while 1:g=(r+k);f=(r-k);r,k=g,f;print(r,k)

r(10,2)

print(len("""def r(r,k):
 while 1:g=(r+k);f=(r-k);r,k=g,f;print(r,k)"""))

def y(g):g=str(g);i=len(g);[print(g*(int(g))+('\n'+g+' '*((int(g)*i)-(i*2))+g)*(int(g)-2)+'\n'+g*int(g))if int(g)>1 else print(g*int(g))]

def g(r):
    print(time.time())
    import numpy as np;import math,itertools;i=np.array(r);d=itertools.combinations_with_replacement(range(-51,51),i.shape[0]);x=[]
    while True:
        try:
            f=np.array(next(d));f.shape=(i.shape[0],1)
            if (np.dot(f.transpose(),np.dot(i,f)))>9:
                pass
            else:
                x.append((-(np.dot(f.transpose(),np.dot(i,f)))))
        except:
            break
    print(sum(math.e**b for b in x))
    print(time.time())

def g(r):
    print(time.time())
    import numpy as np;import math,itertools,threading;i=np.array(r);d=itertools.combinations_with_replacement(range(-1000000,1000000),i.shape[0]);x=[]
    def v():
	    k=threading.Timer(60,v)
	    print(sum(x))
	    k.start()
    v()
    while True:
        try:
            f=np.array(next(d));f.shape=(i.shape[0]);e=(-(np.dot(f.transpose(),np.dot(i,f))))
            if not e<-25:
                    x.append(e)
        except:
                break
    print(x)
    print(sum(math.e**u for u in x))
    print(time.time())


###############
## 162 bytes ##
###############

def v(o):
 import re;r=re.sub('[\W+]',' ',o).split();t,p=[],[]
 for u in r:
  if u[0].lower() not in t:p.append(u+' ')
  t.append(u[0].lower())
 print(''.join(p))

###############
## 176 bytes ##
###############
 
def v(o):import re;t,p=[],[];[(t.append(u[0].lower()),p.append(u+' '))if u[0].lower()not in t else t.append(u[0].lower())for u in re.sub('\W+',' ',o).split()];print(''.join(p))

###############
## 138 bytes ##
###############

import re;p=lambda o,t=[]:''.join([y[0]for y in[(u+' ',t.append(u[0].lower()))for u in re.sub('\W+',' ',o).split()if u[0].lower()not in t]])

e=lambda*a:max([i for i in range(1,max(*a)+1)if not sum(g%i for g in[*a])])

def x(h):import re;return re.sub('(?<=[\]\}\)])(?=[\w+\W+])','\n',re.sub('(?<=[^\]\}\)])(?=[\]\}\)])','\n',re.sub('(?<=[\(\{\[])(?=[\w+\W+])','\n',re.sub('(?<=[^\(\[\{])(?=[\(\[\{])',' ',h))))

def x(h):
	import re;z=[];pa1=['}',']',')'];pa2=['{','[','('];ed=[' ']
	for b in h:
		if b in pa1:
			try:
				if not all(j in z[-1]for j in pa1):
					print('a')
					ed.remove(' ')
					z.append('\n'+' '*len(ed)+b)
				else:
					print('b')
					ed.remove(' ')
					z.append('\n'+' '*len(ed)+b)
			except:
				print('c')
				ed.remove(' ')
				z.append(b+'\n'+' '*len(ed))
		elif b in pa2:
			if not all(j in z[-1]for j in pa2):
				print('d')
				ed.append(' ')
				z.append(' '+b+'\n'+' '*len(ed))
			else:
				print('e')
				ed.append(' ')
				z.append(b+'\n'+' '*len(ed))
		else:
			try:
				if any(x in z[-1]for x in pa1):
					z.append('\n'+' '*len(ed)+b)
					print('g')
					ed.append(' ')
				else:
					print('f')
					z.append(b)
			except:
				print('h')
				z.append(b)
	return ''.join(z)

def x(h):
	import re;z=[];pa1=['}',']',')'];pa2=['{','[','('];ed=[];o=[];count=1
	for b in h:
		if b in pa1:
			print('b')
			ed.remove(' ')
			o.append(len(ed))
			count+=1
			m=[o[0+i:2+i]for i in range(0,len(o),2)]
			print('`m`: '+str(m))
			print(str(count)+': '+str(o[-1]))
			print(str(count)+': '+str(len(ed)))
			print([o[-1],len(ed)])
			if [len(ed),o[-1]]in m:
				ed.remove(' ')
			z.append('\n'+' '*len(ed)+b)
		elif b in pa2:
			if not all(j in z[-1]for j in pa2):
				print('d')
				ed.append(' ')
				z.append(' '+b+'\n'+' '*len(ed))
				o.append(len(ed))
			else:
				print('e')
				ed.append(' ')
				z.append(b+'\n'+' '*len(ed))
				o.append(len(ed))
		else:
			try:
				if any(x in z[-1]for x in pa1):
					z.append('\n'+' '*len(ed)+b)
					print('g')
					ed.append(' ')
					o.append(len(ed))
				else:
					print('f')
					z.append(b)
			except:
				print('h')
				z.append(b)
	print(z)
	return ''.join(z)

def d(x):
        vowels=['a','e','i','o','u']
        for i in x:
                if i.lower()in vowels:
                        print(' \033[1A'+i)
                elif not i.isalnum():
                        print('\n'+i)
                else:
                        print(i)
                        
def d(o):
        vowels=['a','e','i','o','u']
        [print(' \033[1A'+i,end='')if i.lower() in vowels else print('\n'+i,end='')if not i.isalnum()else print(i,end='')for i in o]

def d(*args):
	import itertools;u=[args[0+i:2+i]for i in range(0,len(args),2)];r=[l for l in itertools.combinations(u,2)];print(r);count=0
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

def x(s):
	import numpy as np;from collections import deque as de;y=[''];l=['#'];k=de(' ')
	for z in s[::-1]:
		y.append(z)
	y=y[::-1]
	for h in range(len(y)):
		u=y.pop()
		if len(l)<2:
			k.appendleft(u)
			p=((2**(len(k)-1))-1)
			l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
		else:
			if len(l)>2:
				del l[0]
			p=((2**(len(k)-1))-1)
			a=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%((p*2)+2)==0 and _!=(((p*2)+2)*(p))]
			b=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%(int(((p*2)+2)/2))==0 and _!=(int(((p*2)+2)/2)*((p)*2))and _ not in[g for i in a for g in i]]
			zero=[g for i in a[:len(a)-(int(len(a)/2)):1]for g in i]
			one=[g for i in b[:len(b)-(int(len(b)/2)):1]for g in i]
			two=[g for i in a[len(a)-(int(len(a)/2)):len(a):1]for g in i]
			three=[g for i in b[len(b)-(int(len(b)/2)):len(b):1]for g in i]
			f=list(l[1])
			for i in list(''.join(l[0].split('\n'))):
				if u==0:
					f[zero[0]]=i
					del zero[0]
				elif u==1:
					f[one[0]]=i
					del one[0]
				elif u==2:
					f[two[0]]=i
					del two[0]
				elif u==3:
					f[three[0]]=i
					del three[0]
			del l[0]
			k.appendleft(u)
			p=((2**(len(k)-1))-1)
			l.append(''.join(f))
			l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
	print(''.join(l[-2]))

##################
# Golfed Version #
##################

def x2(s):
 y=[''];l=['#'];k=[' ']
 for z in s[::-1]:y.append(z)
 y=y[::-1]
 for h in range(len(y)):
  if y[-1]!='':u=(int(y.pop())&3)
  else:u=y.pop()
  if len(l)<2:k.append(u);p=((2**(len(k)-1))-1);l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
  else:
   if len(l)>2:del l[0]
   p=((2**(len(k)-1))-1);a=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%((p*2)+2)==0 and _!=(((p*2)+2)*(p))];b=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%(int(((p*2)+2)/2))==0 and _!=(int(((p*2)+2)/2)*((p)*2))and _ not in[g for i in a for g in i]];W=[g for i in a[:len(a)-(int(len(a)/2)):1]for g in i];B=[g for i in b[:len(b)-(int(len(b)/2)):1]for g in i];C=[g for i in a[len(a)-(int(len(a)/2)):len(a):1]for g in i];T=[g for i in b[len(b)-(int(len(b)/2)):len(b):1]for g in i];f=list(l[1])
   for i in list(''.join(l[0].split())):
    if u==0:f[W[0]]=i;del W[0]
    elif u==1:f[B[0]]=i;del B[0]
    elif u==2:f[C[0]]=i;del C[0]
    elif u==3:f[T[0]]=i;del T[0]
   del l[0];k.append(u);p=((2**(len(k)-1))-1);l.append(''.join(f));l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
 print(l[-2])

#####################################
# Ungolfed Version with explanation #
#####################################

def x3(s):
 # Create 3 lists:
 # `y` is for the values of `s` (the list provided) and an empty element for the first pattern
 # `l` is reserved for the pattersn created through each item in list `y`
 # `k` is created for the value of `p` which is the main value through which the pattern is created.
 y=[''];l=['#'];k=[' ']
 # Reverse s, and then add each element from `s` to `y` (in addition to the empty element) 
 for z in s[::-1]:
     y.append(z)
 # `y` should now equal the list created, but reversed
 # If not reversed, then, if, for instance, the input is `0,1,2` and list `y` therefore contains `'',2,1,0`, the empty element will be called at the end, which is NOT what we want).
 y=y[::-1]
 # The main loop; will be iterated through the length of `y` number of times
 for h in range(len(y)):
  # Here is where each element from the end of `y` is recieved as `u` for use in the pattern in each iteration.
  # As you can also see, a bitwise operator (`&`) is used here so that ALL numbers can be accepted. Not just those in the range `0-4`. However, that will happen only if the value of y[-1] (the last elment in y) is NOT ''.
  if y[-1]!='':
      u=(int(y.pop())&3)
  else:
      u=y.pop()
  # If the length of list `l` is less than 2 (which means it only contains `#`), then do the following:
  if len(l)<2:
      # Append `u` to `k`
      k.append(u)
      # Use the length of `k` as `n` in the operation `(2^(n-1)-1)` to get the length of the dot filled part of the pattern.
      p=((2**(len(k)-1))-1)
      # Add that pattern to the list (currently empty, i.e. containing no other pattern in any other quadrant)
      l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
  # Now, if the length of l is >=2, do the following:
  else:
   # If the length of l is >2, then delete the first element in list `l` (this will happen only once, when the `#` is still the first element)
   if len(l)>2:
       del l[0]
   # Again, use the length of `k` as `n` in the operation `(2^(n-1)-1)` to get the length of the dot filled part of the pattern.
   p=((2**(len(k)-1))-1)
   # Create a list with all the index values of all the elements on the left hand side of the list, and also the index value + i where i is every integer in the range `0-p` (this way, it will create lists within a list, each which contain `p` number of integers, which are all indexes of all the dots on the very left side of the grid) 
   a=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%((p*2)+2)==0 and _!=(((p*2)+2)*(p))]
   # Create another list with all the index values of the dots using the same strategy as above, but this time, those in the right half of the grid. 
   b=[[_+i for i in range(p)]for _ in range(len(l[1]))if _%(int(((p*2)+2)/2))==0 and _!=(int(((p*2)+2)/2)*((p)*2))and _ not in[g for i in a for g in i]]
   # Create 4 lists, each containing index values specific to each of the 4 quadrants of th grid
   # W is the list, based on A, containing all the indexes for the 1st quadrant of the grid in l[-1] containing dots (index 0 in the grid)
   W=[g for i in a[:len(a)-(int(len(a)/2)):1]for g in i]
   # B is the list, this time based on b, containing all indexes for the 2nd dot-filled quadrant of the grid l[-1] (index 1 in the grid)
   B=[g for i in b[:len(b)-(int(len(b)/2)):1]for g in i]
   # C is the list, also, like W, based on a, containg all the index values for the 3rd dot-filled quadrant of the grid in l[-1] (index 2 in the grid)
   C=[g for i in a[len(a)-(int(len(a)/2)):len(a):1]for g in i]
   # T is the final list, which, also like B, is based on b, and contains all the index values for the final (4th) dot-filled quadrant of the grid in l[-1] 
   T=[g for i in b[len(b)-(int(len(b)/2)):len(b):1]for g in i];f=list(l[1])
   # Finally, in this `for` loop, utilize all the above lists to create the new pattern, using the last two element in list `l`, where each character of grid l[-2] (the second to last element) is added to the correct index of grid l[-1] based on the value of `u`
   for i in list(''.join(l[0].split())):
    if u==0:
        f[W[0]]=i
        del W[0]
    elif u==1:
        f[B[0]]=i
        del B[0]
    elif u==2:
        f[C[0]]=i
        del C[0]
    elif u==3:
        f[T[0]]=i
        del T[0]
   # Delete the very first element of `l`, as it is now not needed anymore
   del l[0]
   # Append `u` to list`k` at the end of the loop this time
   k.append(u)
   # Update the value of `p` with the new value of length(k)
   p=((2**(len(k)-1))-1)
   # Append the new patter created from the for-loop above to list `l`
   l.append(''.join(f))
   # Append a new, empty pattern to list `l` for use in the next iteration
   l.append((('.'*p+'#'+'.'*p+'\n')*p)+'#'*((p*2)+1)+'\n'+(('.'*p+'#'+'.'*p+'\n')*p))
 # When the above main loop is all finished, print out the second-to-last elment in list `l` as the very last element is the new, empty grid created just in case there is another iteration
 print(l[-2])

def r(o,c=0):
 y=[[j%i for i in range(2,100)]for j in range(o+1)]
 while 1:
  c+=1;z=y[-1][:c:]
  if z not in[f[:c:]for f in y[:-1:]]:break
 print(z)

def g(z):B=z.split();M='i[::-1].translate({41:40,40:41,125:123,123:125,62:60,60:62,93:91,91:93})';r=[*'()[]{}<>'];p=[''.join(u)for u in permutations(B+[eval(M)for i in B if eval(M)not in B],len(B))];l=[''.join([j for j in u[1:-1]if j in r])for u in p];c=[k for k in l if all(b in[i*2for i in r]for y in[[''.join(k)[0+i:2+i]for i in range(0,len(k),2)]]for b in y)];return p[l.index(c[0])]if len(c)else''

def z(e):
	r=[]
	for i in e:
		if i=='+':
			y=[r.pop()for _ in range(2)]
			if len(r)==2:
				r.clear()
			r.append(sum(y))
		elif i=='*':
			y=[r.pop()for _ in range(2)]
			if len(r)==2:
				r.clear()
			r.append(y[0]*y[1])
		elif i==':':
			r.append(r[-1])
		elif i=='/':
			y=[r.pop()for _ in range(2)][::-1]
			if len(r)==2:
				r.clear()
			r.append(y[0]/y[1])
		elif i=='-':
			y=[r.pop()for _ in range(2)][::-1]
			if len(r)==2:
				r.clear()
			r.append(y[0]-y[1])
		else:
			r.append(int(i))
		print(r)
	print(''.join([str(w)for w in r]))

def v(l):
 r={'FG':3,'TD':6,'XP':1,'XD':2,'S':2,'FCK':3};z={i.lower():r[i]for i in r.keys()};a,h,c=[],[],[]
 for g in l:
  c.append(g)
  if''.join(c)in r.keys():h.append(r[''.join(c)]);c.clear()
  elif''.join(c)in z.keys():a.append(z[''.join(c)]);c.clear()
 x,b=max([sum(h),sum(a)]),min([sum(h),sum(a)])
 if sum(h)>sum(a):print(str(x)+' TO '+str(b))
 elif sum(a)>sum(h):print(str(x)+' to '+str(b))
 else:print(str(x)+' To '+str(b))

def v2(l):
 r={'FG':3,'TD':6,'XP':1,'XD':2,'S':2,'FCK':3};z={i.lower():r[i]for i in r.keys()};a,h,c=[],[],[];G=''
 for g in l:
  c.append(g)
  if''.join(c)in r.keys():h.append(r[''.join(c)]);c.clear();G=' TO '
  elif''.join(c)in z.keys():a.append(z[''.join(c)]);c.clear();G=' to '
 x,b=max([sum(h),sum(a)]),min([sum(h),sum(a)])
 if sum(h)==sum(a):print(str(x)+' To '+str(b))
 else:print(str(x)+G+str(b))

def g2(z):B=z.split();print(B);k=lambda y:{'<':0,'>':0,'{':0,'}':0,'[':0,']':0,'('0,')':0}[y]+=1;M='i[::-1].translate({41:40,40:41,125:123,123:125,62:60,60:62,93:91,91:93})';f=B+[eval(M)for i in B if eval(M)not in B];print(f);c=[j[0]for j in f];x=[f[0]];print(c);[x.append(c[k[-1]])for k in x if len(x)<len(B)and k[-1]in c.keys()and c[k[-1]]not in x];return''.join(x)if len(x)>=len(B)else''

def g3(z):
 B=z.split();M='i[::-1].translate({41:40,40:41,125:123,123:125,62:60,60:62,93:91,91:93})';f=B+[eval(M)for i in B if eval(M)not in B];d=[f.pop(0)]
 for h in d:
  try:[d.append([f.pop(f.index(c))for c in f if h[-1]==c[0]][0])if len(d)<len(B)else E]
  except:break
 return''.join(d)if len(d)>=len(B)else''

def g4(z):B=z.split();M='i[::-1].translate({41:40,40:41,125:123,123:125,62:60,60:62,93:91,91:93})';f=B+[eval(M)for i in B if eval(M)not in B];d=[f.pop(0)];[d.append([f.pop(f.index(c))for c in f if h[-1]==c[0]][0])for h in d if len([f[f.index(c)]for c in f if h[-1]==c[0]])];return''.join(d)if len(d)>=len(B)else''

def a(t):B=t.split();w=[''.join(str(i[0])+str(i[1]))for i in[i for i in combinations_with_replacement(range(7),2)]];w=[i[::-1]for i in w]if any(i in B for i in[str(q)+'0'for q in range(1,7)])else w;return[i for i in w if i not in B]

def j(r):
	e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o))

def j2(r):
	e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u)+''.join(o))

def j3(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u)+''.join(o))

def j4(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u),end='');print(''.join(['| '*5+o[0].strip('\n')+' |'*6+'\n']+['| '*4+'+'+'-'+o[1].strip('\n')+'-'+'+'+' |'*5+'\n']+['| '*g+'+'+'-'*(7-(i.count('-')//2))+i.strip('\n')+'-'*(7-(i.count('-')//2))+'+'+' |'*(g+1)+'\n'for g,i in zip(list(range(3,0,-1)),o[2:])]))

def j5(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u),end='');print(''.join(['| '*((r+3)*(r+1)-((r+3)-1))+o[0].strip('\n')+' |'*((r+3)*(r+1)-((r+3)-2))+'\n']+['| '*((r+3)*(r+1)-(r+3))+'+'+'-'+o[1].strip('\n')+'-'+'+'+' |'*((r+3)*(r+1)-((r+3)-1)))+'\n']+['| '*g+'+'+'-'*(7-(i.count('-')//2))+i.strip('\n')+'-'*(7-(i.count('-')//2))+'+'+' |'*(g+1)+'\n'for g,i in zip(list(range(((r+3)*(r+1)-((r+3)+1)),0,-1)),o[2:])]))

def j6(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u),end='');P=['| '*g+'+'*o+'-'*k+q.strip('\n')+'-'*k+'+'*o+' |'*(g+1)+'\n'for g,o,k,q in zip(list(range((4*(r+1))-(2+r),0,-1)),[0]+[1]*(len(o)-1),[0]+list(range(1,(4*(r+1)),2)),o)];print(''.join(P))

def j7(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];print(q[::-1]+q[1:]);o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]+q[1:]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u),end='');P=['| '*g+'+'*o+'-'*k+q.strip('\n')+'-'*k+'+'*o+' |'*(g+1)+'\n'for g,o,k,q in zip(list(range((4*(r+1))-(2+r),0,-1))+list(range(0,(4*(r+1))-(2+r),1)),[0]+[1]*(len(o)-1),[0]+list(range(1,(4*(r+1)),2))+list(range((4*(r+1))+1,11*r,2)),o)];print(''.join(P),end='')

def j8(r):e=[u for u in range(0,r+(r+1),2)];p=[y for y in range(r+(r+1),0,-2)];q=[o for o in zip(e,p)];o=['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q]+['-'*(r+(r+2))+'+'+'-'*(r+(r+2))+'\n']+['-'*y+'+'+' '+'| '*b+'+'+'-'*y+'\n'for y,b in q[::-1]+q[1:]];print(''.join(o));z=[1];[z.append(i+4)for i in z if len(z)<(4*(r+1))];z=z[::-1];J=[i for i in range(4*(r+1))];d=[g for g in zip(z,J)];u=['| '*w+'+'+'-'*v+'+'+' |'*w+'\n'for v,w in d];print(''.join(u),end='');P=['| '*g+'+'*o+'-'*k+q.strip('\n')+'-'*k+'+'*o+' |'*(g+1)+'\n'for g,o,k,q in zip(list(range((4*(r+1))-(2+r),0,-1))+list(range(0,(4*(r+1))-(2+r),1)),[0]+[1]*(len(o)-1),[0]+list(range(1,(4*(r+1)),2))+list(range((4*(r+1))+1,11*r,2)),o)];print(''.join(P),end='');F=[' '*(len(P[-1].split()[0])+1)+'+'+'-'*(P[-1].split()[0].count('-')+4)+'+'];print(''.join(F))

##################################
# `j9` Completed @ 411 bytes! :) #
##################################

def j9(r):R=range;Z=zip;B=r+r+2;P,M='+-';X='| ';q=[*Z(R(0,B-1,2),R(B-1,0,-2))];L=r+1;A=2+r;print('\n'.join([X*w+P+M*v+P+' |'*w for v,w in Z(R(4*L*4-3,0,-4),R(4*L))]+[X*g+P*o+M*k+u+M*k+P*o+' |'*-~g for g,o,k,u in Z([*R(4*L-A,0,-1),*R(4*L-A)],[0]+[1]*(3*r+2),[0,*R(1,4*L,2),*R(4*L+1,11*r,2)],[M*y+'+ '+X*b+P+M*y for y,b in q]+[M*B+P+M*B]+[M*y+'+ '+X*b+P+M*y for y,b in q[::-1]+q[1:]])]+[' '*(8*r+6)+P+M*(8*r+7)+P]))

def p(u):i={(255,0,0):'Red',(0,0,255):'Blue',(0,255,0):'Green',(255,255,0):'Yellow',(128,0,128):'Purple',(128,128,128):'Gray',(0,0,0):'Black'};k=[*u.strip('#')];print(i[tuple([0if x<100else 128if x<200else 255for x in[int(''.join(p),16)for p in[k[i:2+i]for i in range(0,len(k),2)]]])])

def g(f,a,n,L=len,S=str):import math,re;A=S(a);print('+'.join(t.replace('x',A)+re.sub('(\W\(x-\d+\)\^0|/1|\*1|\^1|\*0)(?!\d+)','',g)for t,g in zip(f*(n//L(f))+f[:n%L(f)],['*'+A+'/'+S(math.factorial(n))+'*'+'(x-'+A+')^'+S(n)for n in range(n)])).replace('+-','-').replace('--','+').replace('x-0','x'))

##################################
# `u` completed at 281 bytes! :) #
##################################

def u(z):
 p=[];P=print;S,N,M,X=' -|\n'
 while not p or z:p+=[z%20];z=z//20
 E=lambda i:(S+N*4+S)*i+X+((M+S*4+M)*i+X)*2+(S+N*4+S)*i+X;F=N*32+X+M+S*30+M+X+N*32+X;[P(S+N*19+S+X+M+((S*4+M)*4+X+M)*2+N*19+M+X+(M+S*19+M+X)*2+S+N*19+S+X*3)if y<1else P(E(y%5)+F*(y//5)+X*3)for y in p[::-1]]

f=lambda g,f:''.join((g*len(f))[i:i+3]for i in range(0,len(f)*3,3))

q=lambda w:((1+sum(w))%65521)+4**8*(sum(1+sum(w[:i+1])for i in range(len(w)))%65521)

def k(u,*p):
 import itertools as i,random as r;y=[]
 for z in p:y+=[''.join(i)for i in i.product(*[u[i]for o in z for i in o])]
 for q in'1'*100:print(''.join([r.choice(y)for i in'1'*r.randint(1,5)]))

def k2(u,*p):import itertools as i,random as r;R=r.choice;y=[];o=[];[y.extend([''.join(i)for i in set(i.product(*[u[i]for o in z for i in o]))])for z in p];[o.extend([''.join([R(y)for i in range(R(range(1,6)))])])for q in '1'*100];print(o)

def r(n,c,h):x=[' '*(i)+'/'+'-'*(n-2)+'/'for i in range(h,0,-1)];d=['|'+'-'*(n-2)+'| |\n'for q in range(c-h)];v=['|'+'_'*(n-2)+'|'+' '*(i-1)+'/'for i in range(h,0,-1)];print('\n'.join([x[0],x[1].replace('-',' ')+'|','\n'.join(x[2:]).replace('-',' ')])+''.join([d[0],''.join(d[1:]).replace('-',' ')])+'\n'.join([''.join(v[:-1]).replace('_',' '),v[-1]]))

def s(w,h,d):R=range;S,V,L=' |/';O=w-2;U=d-h;print('\n'.join([S*(d-i)+L+' -'[i<1]*O+L+S*i+V for i in R(d-max(0,U))]+[S*(U-i)+L+S*O+L+S*(h-1)+L for i in R(U)]+[V+z(q)*O+V+S*d+V for q in R(h-d)]+[V+[' -'[i==h],'_'][i<2]*O+V+S*(i-1)+L for i in R(h-max(0,h-d),0,-1)]))

###################################
# `s2` completed at 248 bytes! :) #
###################################

def s2(w,h,d):R,M=range,max;S,V,L=' |/';O=w-2;D=d-M(0,d-h);Q=h-M(0,h-d);print('\n'.join([S*(d-i)+L+' -'[i<1]*O+L+S*[h-1,i][i<=D-1]+'/|'[i<=D-1]for i in R(D+M(0,d-h))]+[V+[' -'[i==h],'_'][i<2]*O+V+S*[i-1,d][i>Q]+'/|'[i>Q]for i in R(Q+M(0,h-d),0,-1)]))

def g(o):import urllib.request as u,re;R=re.findall;w=bytes.decode(u.urlopen('http://ppcg.lol/q/'+o).read());print(len(R('(?:<h[0-9]>|<p>).*python',w.lower()))<2and int(R('(?<="vote-count-post ">)[0-9]+',w)[0])>3and w.count('answercell">')>5)

def g2(o):import urllib.request as u,re;R=re.findall;w=bytes.decode(u.urlopen('http://ppcg.lol/q/'+o).read());print(len(R('(?<=answercell">)(?s)(.+?)(<h[0-9]>|<p>)python(.+?)\n',w.lower()))<2and int(R('(?<="vote-count-post ">)[0-9]+',w)[0])>3and int(R('(?:answers-subheader">\s+<h2>\s+)([0-9]+)',w)[0])>5)

def g3(o):import urllib.request as u,re;R=re.findall;w=bytes.decode(u.urlopen('http://ppcg.lol/q/'+o).read());print(len(R('answercell">.\s+.+\s+(?:<h[0-9]>|<p>).*python.*(?:</h[0-9]>|</p>)',w.lower()))<2and int(R('(?<="vote-count-post ">)[0-9]+',w)[0])>3and w.count('answercell">')>5)

def g4(o):
 import urllib.request as u,re;R=re.findall;w=bytes.decode(u.urlopen('http://ppcg.lol/q/'+o).read());t=0if len(re.findall('="go to page ([0-9]+)">',w))<1else max([int(i)for i in re.findall('="go to page ([0-9]+)">',w)])
 if t<1:print(len(R('(?<=answercell">).*?(?:<h[0-9]>|<strong>)[^\n]*python[^\n]*(?=</h[0-9]>|</strong>)',w.lower(),re.DOTALL))<2and int(R('(?<="vote-count-post ">)[0-9]+',w)[0])>3and w.count('answercell">')>5)
 else:
  P=[];U=[];K=[]
  for i in range(2,t+2):P.append(len(R('(?<=answercell">).*?(?:<h[0-9]>|<strong>)[^\n]*python[^\n]*(?=</h[0-9]>|</strong>)',w.lower(),re.DOTALL)));U.append(int(R('(?<="vote-count-post ">)[0-9]+',w)[0]));K.append(w.count('answercell">'));w=bytes.decode(u.urlopen('http://ppcg.lol/questions/'+o+'/?page='+str(i)).read())
  print(sum(P)<2and U[0]>3and sum(K)>5);print('# Python answers: ',sum(P));print('# Votes: ',U[0]);print('# Answers: ',sum(K))

def g5(o):import urllib.request as u,re;R=re.findall;w=bytes.decode(u.urlopen('http://ppcg.lol/q/'+o).read());print(len(R('(?<=answercell">).*?(?:<h[0-9]>|<strong>)[^\n]*python[^\n]*(?=</h[0-9]>|</strong>)',w.lower()))<2and int(R('(?<="vote-count-post ">)[0-9]+',w)[0])>3and w.count('answercell">')>5)

def c(u):import re;q=re.findall(r"\b['\-\w]+\b",u.lower());Q=q.count;D=[*map(Q,{*q})];return['',max(q,key=Q)][1in map(D.count,D)]

def c2(u):import re;q=''.join([i for i in u.lower()if i in[*map(chr,range(97,123)),*"'- "]]).split();Q=q.count;D=[*map(Q,{*q})];return['',max(q,key=Q)][1in map(D.count,D)]
