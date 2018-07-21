# The Challenge: http://codegolf.stackexchange.com/questions/81035/collide-against-walls

# First Steps
u=list('+'+'-'*35+'+\n'+('|'+' '*35+'|\n')*15+'+'+'-'*35+'+')
for g in[i for i in range(u.index(' '),u.index(' ')+(35*16),39)]:
    u[g] = 'o'

