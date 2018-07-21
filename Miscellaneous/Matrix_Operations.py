# Transpose a Matrix
Transpose=lambda O:[[O[i][g]for i in range(len(O))]for g in range(len(O[0]))]

# Find the dot product of any two input LxN and NxP matrices
Dot_Product=lambda A,B:[[sum([i*g for i,g in zip(A[i],Transpose(B)[q])])for q in range(len(B[0]))]for i in range(len(A))]if len(A[0])==len(B)else'Columns not equal to rows!'

# Recursively find determinent of any NxN matrix
Determinent=lambda O:sum([eval('+-'[i%2]+str(O[0][i]))*Determinent([[e[q]for q in range(len(e))if q!=i]for e in O[1:]])for i in range(len(O))])if len(O)>2else O[0][0]*O[1][1]-O[0][1]*O[1][0]

# Iteratively find inverse of any NxN matrix using above Determinent function in Adjoint Method (Inv(A)=Adj(A)/Det(A);Proof of Formula @ https://www.youtube.com/watch?v=L6APsIqyx-k); Throws `Zero Division Error` if determinent is 0
Inverse=lambda O:[[Transpose([[eval('+-'[(len(O)*i+n)%2if len(O)%2>0else (len(O)*i+n)%2==[1,0][i%2]]+str(Determinent(v)))for n,v in enumerate(zip(*[[[O[g][m]for m in range(len(O))if m!=k]for k in range(len(O))]for g in range(len(O))if g!=i]))]for i in range(len(O))])[g][i]*(1/Determinent(O))for i in range(len(O))]for g in range(len(O))]if len(O)>2else[[[[O[1][1],-O[0][1]],[-O[1][0],O[0][0]]][g][i]*(1/Determinent(O))for i in range(2)]for g in range(2)]

# Solve an input system of linear equations using Matrix Method. Takes each equation as a string in the format `Ax+By+Cz+...=D` and only works for *determined systems*, i.e. only those where the number of equations are the same as the number of variables to be solved for. Therefore, it (currently) does *not* work for overdetermined (no. equations more than no. variables) or underdetermined (no. variables more than no. equations) systems.
Linear_Equations_Solver=lambda*a,re=__import__('re'):Dot_Product(Inverse([[float(i)for i in re.findall('-?[\d.]+',s)[:-1]]for s in a]),[[int(re.findall('-?[\d.]+',s)[-1])]for s in a])

# Solve for a polynomial based on a given set of input and corresponding output points; Takes input in format `Xlist,Ylist`; Based off of challenge @ http://codegolf.stackexchange.com/questions/1729/polynomial-interpolation
Polynomial_Interpolation=lambda L,M,Fraction=__import__('fractions').Fraction,W=lambda u:abs(__import__('fractions').Fraction(round(u,15)).limit_denominator()):'f(x)='+''.join([('+'*(i[0]>0)+str(int(i[0]))if round(i[0],5).is_integer()else'+-'[i[0]<0]+'\\frac{'+str(W(i[0]).numerator)+'}{'+str(W(i[0]).denominator)+'}')+'x'*(f>0)+'^%d'%f*(f>1)for f,i in enumerate(Dot_Product(Inverse([[L[g]**h for h in range(~-len(L),-1,-1)]for g in range(len(L))]),[[i]for i in M])[::-1])if round(i[0],5)!=0][::-1]).replace('+-','-').strip('+')

# Version of Polynomial Interpolation which returns list of coefficents rather than LaTeX formatted string; Uses same input format as other version
Polynomial_Interpolation_Simple=lambda L,M:Dot_Product(Inverse([[L[g]**h for h in range(~-len(L),-1,-1)]for g in range(len(L))]),[[i]for i in M])

##############################################################################################################################################################
# Definite Integral Calculators, each using different method to calculate area; Given function `f', inclusive interval [a,b] and number of sub-intervals `N' #
##############################################################################################################################################################

# Using Simpson's Method - http://tutorial.math.lamar.edu/Classes/CalcII/ApproximatingDefIntegrals.aspx
# Utilizes quadratics rather than lines for each sub-interval to best-fit curve
# Fastest converging of all methods presented here for non-linear functions.
def Area_Simpsons(f,a,b,N):
     Total = 0;
     for i in range(1, N + 1):
             Left = (a + (b - a) * (i - 1) / N)
             Mid = (a + (b - a) * (i - 1/2) / N) 
             Right = (a + (b - a) * i / N)
             Values = Polynomial_Interpolation_Simple([Left, Mid, Right], [f(Left), f(Mid), f(Right)])
             Total += Values[0][0] * (Right**3 - Left**3)/3 + Values[1][0] * (Right**2 - Left**2) / 2 + Values[2][0] * (Right - Left)
     return Total

# Using Trapezoid Riemann Sum
# Fasted converging of all methods presented here for linear functions.
def Area_Trapezoid(f,a,b,N):
    Total = 0;
    for u in range(1, N+1):
        Total += (f(a + (b - a) * (u - 1) / N) + f(a + (b - a) * u / N)) / 2 * ((b - a) / N)
    return Total

# Using Right Riemann Sum
def Area_Right(f,a,b,N):
    Total = 0;
    for u in range(1, N+1):
        Total += f(a + (b - a) * (u - 1) / N) * ((b - a) / N)
    return Total

# Using Left Riemann Sum
def Area_Left(f,a,b,N):
    Total = 0
    for u in range(1, N+1):
        Total += f(a + (b - a) * u / N) * ((b - a) / N)
    return Total

# Using Midpoint Riemann Sum
def Area_Midpoint(f,a,b,N):
    Total = 0
    for u in range(1,N+1):
        Total += f(a + (b - a) * (u - 1/2) / N) * ((b - a) / N)
    return Total

if __name__ == '__main__':
     # Here is an example of `Polynomial_Interpolation' in action
     print(Polynomial_Interpolation([4/3,2,-8/3,-5,0],[617/81,20/3,6749/81,7367/12,23/3]))
     # Same thing with `Polynomial_Interpolation_Simple'
     print(Polynomial_Interpolation_Simple([4/3,2,-8/3,-5,0],[617/81,20/3,6749/81,7367/12,23/3]),'\n')

     # Euler's Number
     e = 2.7182818284590452353602874713527

     # Numerically approximate the Gamma function: https://en.wikipedia.org/wiki/Gamma_function
     # Expected Result: https://www.wolframalpha.com/input/?i=Gamma(2.5)
     # The following will approximate Gamma(2.5)
     F2 = lambda x:(x**1.5)*e**(-x)
     print("Gamma(%f) = %.16f\n"%(2.5,Area_Simpsons(F2,0,1000,10000)))
     
     # See each of the definite integration methods in action for all integers in interval [1,1000]
     # For reference, the actual value for the definite integral of f(x) = e**x**2 on interval [0,2] as calculated by Desmos is ~16.4526277655
     # Same thing with Wolfram Alpha - https://www.wolframalpha.com/input/?i=definite+integral+of+e%5Ex%5E2+on+%5B0,2%5D+to+16+sig+figs
     # Same thing with the Online Integral Calculator - http://www.integral-calculator.com/#expr=e%5Ex%5E2&lbound=0&ubound=2&numonly=1
     F = lambda x:e**x**2
     for i in range(1,111):
          print('i =','%04d'%i,': Simpson\'s Method ->','%.16f'%Area_Simpsons(F,0,2,i),'vs. Trapezoid Riemann Sum ->','%.16f'%Area_Trapezoid(F,0,2,i),'vs. Right Riemann Sum ->','%.16f'%Area_Right(F,0,2,i),'vs. Left Riemann Sum ->','%.16f'%Area_Left(F,0,2,i),'vs. Midpoint Riemann Sum ->','%.16f'%Area_Midpoint(F,0,2,i))
