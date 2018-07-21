###################################################################################################
# My own custom Permutation and Combination finding functions w/out use of any external libraries #
# Takes Input as `<C/P(Combinate/Permute)> <Y/N(Count/List)> <No. Elements> <No. Spots>`          #
###################################################################################################

import sys # <- Used to collect  command line input
import time

Q=time.time()

############################################################################
# First version: Works correctly ONLY for numbers in Inclusive Range [1,9] #
############################################################################
Combinate=lambda g,a:{*map(lambda g:''.join(sorted(str(g))),[i for i in range(int(''.join(str(u)for u in range(1,a+1))),int(''.join(str(u)for u in range(g,g-a,-1)))+1)if len({*str(i)})==len(str(i))==a and max(map(int,[*str(i)]))in range(g,a-1,-1)and min(map(int,[*str(i)]))in range(1,g+1)])}
Permutate=lambda g,a:[i for i in range(int(''.join(str(u)for u in range(1,a+1))),int(''.join(str(u)for u in range(g,g-a,-1)))+1)if len({*str(i)})==len(str(i))==a and max(map(int,[*str(i)]))in range(g,a-1,-1)and min(map(int,[*str(i)]))in range(1,g+1)]

#############################################################################
# Second version: Works correctly for ALL natural numbers; CURRENTLY IN USE #
#############################################################################
Permutate2=lambda X,M:sorted({i for i in eval(('[('+'%s,'*M+')'+('for %s in range(1,'+str(X)+'+1)')*M+']')%tuple([chr(i)for i in range(65,65+M)]*2))if len({*i})==len(i)})if X>=M else[]
Combinate2=lambda X,M:sorted({i for i in eval(('[tuple(sorted(('+'%s,'*M+')))'+('for %s in range(1,'+str(X)+'+1)')*M+']')%tuple([chr(i)for i in range(65,65+M)]*2))if len({*i})==len(i)})

######################################################################################################################################################
# Third Version: Same as Second, but now instead takes in an array of items as first input, and can take into consideration repetitions in the array #
# (https://www.mathsisfun.com/combinatorics/combinations-permutations.html)                                                                          #
# (http://www.regentsprep.org/regents/math/algebra/APR2/LpermRep.htm)                                                                                #
######################################################################################################################################################
Permutate3=lambda X,M:sorted({i for i in eval(('[('+(str(X)+'[%s],')*M+')'+('for %s in range('+str(len(X))+')')*M+']')%tuple([chr(i)for i in range(65,65+M)]*2))if all(i.count(u)<=X.count(u)for u in{*X})})
Combinate3=lambda X,M:sorted({i for i in eval(('[tuple(sorted(['+(str(X)+'[%s],')*M+']))'+('for %s in range('+str(len(X))+')')*M+']')%tuple([chr(i)for i in range(65,65+M)]*2))if all(i.count(u)<=X.count(u)for u in{*X})})

T=map(int,sys.argv[3:])

# assert 0<int(sys.argv[3])<10,'Number of elements over 9 currently not supported!'
assert int(sys.argv[3])>=int(sys.argv[4]),'Number of spots available must be less than or equal to the number of elements!'
assert int(sys.argv[4])>0 and int(sys.argv[3])>0,'Number of slots and elements must be more than 0!'

if sys.argv[1]=='C':
    if sys.argv[2]=='Y':
        print(len(Combinate2(*T)))
    elif sys.argv[2]=='N':
        print(Combinate2(*T))
elif sys.argv[1]=='P':
    if sys.argv[2]=='Y':
        print(len(Permutate2(*T)))
    elif sys.argv[2]=='N':
        print(Permutate2(*T))

print('Time Taken in seconds:',time.time()-Q)
              
