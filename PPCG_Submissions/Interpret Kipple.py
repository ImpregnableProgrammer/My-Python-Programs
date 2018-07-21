# This Challenge: http://codegolf.stackexchange.com/questions/84914/interpret-kipple

def T(p):
    S={i:[0]for i in[*map(chr,range(97,123)),'@']}
    S['i']+=[*map(int,input().split(' '))]



T('a')
