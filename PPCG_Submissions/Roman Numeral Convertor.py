def F(o):
    T={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M',5e3:'¯V',9e3:'M¯X',1e4:'¯X'}
    Z=''
    while o:
        U=[i for i in sorted(T.keys())if i<=o]
        Z+=T[U[-1]]
        o-=U[-1]
    print(sum([*bytes(Z,'iso 8859-1')]))

F(2016)