# For this Challenge: http://codegolf.stackexchange.com/questions/86852/leos-pokerface#86852
from random import*
import re
hand=input().split(' ')
Z=randint(0,1)
print(Z)
if Z:
    Y=randint(1,5)
    print(Y)
    for t in range(Y):
        hand.remove(choice(hand))
    hand+=input().split(' ')
R=randint(0,3)
print(R)
if R:
    hand+=input().split(' ')
# F=sorted(hand,key=lambda i:int(i[1].translate(dict(zip([*b'TJQKA'],'ABCD1'))),16))
# print(F)
# # re.fullmatch('.*A.*K.*Q.*J.*T|')
# if sum([i==g+1for i,g in zip(F,F[1:])])>=5:
#     print(F[:5])
# elif






