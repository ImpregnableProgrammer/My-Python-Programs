# This Challenge: http://codegolf.stackexchange.com/questions/92903/decipher-neurotic-frogs/92928#92928
from re import*
def F(i):
 W="";S=split;D='[.,?!:;()"\-]';Q=lambda c,t:len(sub(D,"",c.group()).split()[t])
 for m in S(D+'\n',sub(D+"*\w*\*[A-Za-z0-9']+\*.*?(?=\s) [A-Za-z0-9']+",lambda v:"a"*([20,10][Q(v,0)%2]+Q(v,1)),i.replace("--"," ").replace("'",""))):
  for g in S(D+'  ',m):
   for q in S(D[:-1]+" "+D[-1],g):
    W+=chr(64+len(q))
   W+=" "
  W=W[:-1]+".  "
 print(W.replace("@",""))

F('''Perpendicular l*ou*nging calms.  *A* frog, a m*u*d cap... bliss!  Wallowing g*e*n*e*rates happiness.  Amphibian sp*a* isn't expensive--seventy d*o*llars--cheap!  That'*s* not *a* large e*x*pens*e* from an*y* discerning fr*o*g's money, unlik*e* Super 8.
Ever*y*one--frogs, toad*s*, newts, *a*nd salamanders!  G*e*t a wonderful shiat*s*u, or recei*v*e an other kind.  Masseus*es* are her*e* today!  Invite a fianc*e*e, supervisor, roommate, niece: *all* welcomed!
Y*o*u simply ne*v*er believed these p*o*ssibilitie*s*; they're (I *swear*) absolute truth!  Th*e* Montgomery A*m*phibian Salon!  Come luxuriate today!''')
            
                          
