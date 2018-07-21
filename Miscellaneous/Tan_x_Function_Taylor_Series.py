R=range
# The Kroneker Delta Function
Kroneker=lambda f,k:f==k
# Recursively calculate the factorial of any input integer
Factorial=lambda g:g>1and g*Factorial(g-1)or 1.
# Recursively generate the m'th (widely accepted) Bernoulli number using the formula shown here: https://en.wikipedia.org/wiki/Bernoulli_number#Recursive_definition
Bernoulli=lambda m:Kroneker(m,0)-sum((Factorial(m)*Bernoulli(k)/(Factorial(k)*Factorial(m-k)*(m-k+1)))for k in range(m))
# Calculate the Tan of any angle `x` in *radians* using the explicit Maclaurin Series formula shown at http://mathworld.wolfram.com/MaclaurinSeries.html up to 10 iterations/terms in the expansion
# Domain of accuracy: |x|<pi/2
Tan=lambda x:sum(((-1)**n*2**(2*n+2)*(2**(2*n+2)-1)*Bernoulli(2*n+2)*x**(2*n+1))/Factorial(2*n+2)for n in range(10))
