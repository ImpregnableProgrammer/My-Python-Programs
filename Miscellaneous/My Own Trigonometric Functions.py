from math import pi


class TrigonometricFunctions:

    def __init__(self,p,degrees=False):
        self.Stack = []
        self.p=p
        if degrees:
            self.p=(p*pi)/180
        self.p%=(pi*2)

    def Factorial(self,l):
        f=[1];[f.append(f[-1]*i)for i in range(1,l+1)];return f[-1]

    # Uses Maclaurin Series for sin(x)
    def Sin(self):
        for n in range(100):
            self.Stack.append((((-1)**n)/self.Factorial(2*n+1))*(self.p**(2*n+1)))
        return sum(self.Stack)

    # Uses Maclaurin Series for Cos(x)
    def Cos(self):
        for n in range(101):
            self.Stack.append((((-1)**n)/self.Factorial(2*n))*(self.p**(2*n)))
        return sum(self.Stack)

    # Tan(x) = Sin(x)/Cos(x)
    def Tan(self):
        return self.Sin()/self.Cos()

    # Uses Maclaurin Series for arcsin(x)
    # List "c" contains sequence shown here: https://oeis.org/search?q=-1%2C-1%2C-9%2C-225&language=english&go=Search
    def Arcsin(self):
        def Prod(w):f=[1];[f.append(f[-1]*i)for i in w];return f[-1]
        v=[];c=[]
        for n in range(501):
            v.append(2*n+1)
        for a in range(501):
            c.append(Prod(v[:a])**2)
        for g in range(501):
            self.Stack.append((c[g]/self.Factorial(2*g+1))*(self.p**(2*g+1)))
        if self.p<-1 or self.p>1:
            raise ValueError('Domain Error')
        else:
            return sum(self.Stack)

    # Same thing as above except uses different, more general formula for arcsin(x)
    # Utilizes this sequence: https://oeis.org/search?q=-1%2C-1%2C-9%2C-225&language=english&go=Search
    def Arcsin2(self):
        def Prod(w):f=[1];[f.append(f[-1]*i)for i in w];return f[-1]
        for g in range(1001):
            self.Stack.append(((Prod([(2*k)-1 for k in range(1,g+1)])**2)/self.Factorial(2*g+1))*(self.p**(2*g+1)))
        if self.p<-1 or self.p>1:
            raise ValueError('Domain Error')
        else:
            return sum(self.Stack)

    # Uses Maclaurin Series for arccos(x)
    # List "c" contains sequence shown here: https://oeis.org/search?q=-1%2C-1%2C-9%2C-225&language=english&go=Search
    def Arccos(self):
        def Prod(w):f=[1];[f.append(f[-1]*i)for i in w];return f[-1]
        v=[];c=[]
        for n in range(501):
            v.append(2*n+1)
        for a in range(501):
            c.append(Prod(v[:a])**2)
        for g in range(501):
            self.Stack.append((c[g]/self.Factorial(2*g+1))*(self.p**(2*g+1)))
        if self.p<-1 or self.p>1:
            raise ValueError('Domain Error')
        else:
            return pi/2-sum(self.Stack)

    # Same thing as above except uses different, more general formula to calculate arccos(x)
    # Utilizes this sequence: https://oeis.org/search?q=-1%2C-1%2C-9%2C-225&language=english&go=Search
    def Arccos2(self):
        def Prod(w):f=[1];[f.append(f[-1]*i)for i in w];return f[-1]
        for g in range(501):
            self.Stack.append(((Prod([(2*k)-1 for k in range(1,g+1)])**2)/self.Factorial(2*g+1))*(self.p**(2*g+1)))
        if self.p<-1 or self.p>1:
            raise ValueError('Domain Error')
        else:
            return pi/2-sum(self.Stack)

    # arccos(x) = pi/2 - arcsin(x)
    def Arccos3(self):
        return pi/2-self.Arcsin()

TF = TrigonometricFunctions

if __name__ == '__main__':
    print("Sin:",TF(8,1).Sin(),
          "\nCos:",TF(0.5).Cos(),
          "\nTan:",TF(0.5).Tan(),
          "\nArcsin1:",TF(0.5).Arcsin(),
          "\nArcsin2:",TF(0.5).Arcsin2(),
          "\nArccos1:",TF(0.5).Arccos(),
          "\nArccos2:",TF(0.5).Arccos2(),
          "\nArccos3:",TF(0.5).Arccos3())
