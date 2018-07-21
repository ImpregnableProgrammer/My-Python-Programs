# No External Libraries Used!

def P(r):
    q=[];g=lambda h:h[0]if len(h)<2else g([h[0]*h[1]]+h[2:])
    for i in range(1,r+1):
        q.append(1/g([*range(1,i+1)]))
    print(1+sum(q))

P(1000000)