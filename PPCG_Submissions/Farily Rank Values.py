# The Challenge: http://codegolf.stackexchange.com/questions/81081/fairly-rank-values#81083

def j(p):
 z=sorted(p);u=sorted(enumerate(p,1),key=lambda i:i[1]);q=[i for i,g in enumerate(z,1)if z.count(g)>1];
 l=sum(q)/len(q);print([l if i in q else i for i,g in u])