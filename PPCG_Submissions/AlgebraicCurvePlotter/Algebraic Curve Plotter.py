# This Challenge: http://codegolf.stackexchange.com/questions/86879/algebraic-curve-plotter

# Short Method using numpy and MatPlotLib at 352 bytes
from matplotlib.pyplot import*;from numpy import*
def R(M,S,U,r=range):N=linspace;E='+'.join([str(y)+'*'+m for y,m in[q for i,g in zip(M,[[i+'*'+p for p in['1']+['x^%d'%p for p in r(1,len(M[0]))]]for i in['1']+['y^%d'%i for i in r(1,len(M))]])for q in zip(i,g)if q[0]]]);x,y=meshgrid(N(*S,200),N(*U,200));contour(x,y,eval(E.replace('^','**')),0);show()

for i in[
    ([[-1,0,1],[0,0,0],[1,0,0]],
     [-2,2],
     [-2,2]),
    ([[-1,0,1],[0,0,0],[2,0,0]],
     [-2,2],
     [-1,1]),
    ([[0,0],[0,1]],
     [-1,2],
     [-2,1]),
    ([[0,-1],[0,0],[1,0]],
     [-1,3],
     [-2,2]),
    ([[-1,1,0,-1],[0,0,0,0],[1,0,0,0]],
     [-2,2],
     [-3,3]),
    ([[0,0,0,1],[0,-3,0,0],[0,0,0,0],[1,0,0,0]],
     [-3,3],
     [-3,3]),
    ([[0,0,-1,0,1],[0,0,0,0,0],[1,0,0,0,0]],
     [-2,2],
     [-1,1],),
    ([[0,0,0,-1,1],[0,0,0,0,0],[0,3,2,0,0],[0,0,0,0,0],[1,0,0,0,0]],
     [-1,1],
     [-1,1],),
    ([[-1,0,3,0,-3,0,1],[0,0,0,0,0,0,0],[3,0,21,0,3,0,0],[0,0,0,0,0,0,0],[-3,0,3,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0]],
     [-1,1],
     [-1,1])]:R(*i)




