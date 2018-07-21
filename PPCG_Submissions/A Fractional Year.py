# This Challenge: http://codegolf.stackexchange.com/questions/88924/a-fractional-year

# 192 bytes
def Q(V):import re;A=[*map(lambda y:int(y.strip('0')),re.findall('\d+',V))];return'%.5f'%(A[0]+((sum([[30,31][i%2<1or i==7],28][i==1]for i in range(-~A[1]))+~-A[2])*1440+A[3]*60+A[4])/525600)