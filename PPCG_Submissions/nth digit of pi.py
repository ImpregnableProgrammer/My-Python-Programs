# This Challenge: http://codegolf.stackexchange.com/questions/84444/find-the-nth-decimal-of-pi

# First method – all in 1 line: 226 bytes
# Uses this algorithm: https://en.wikipedia.org/wiki/Gauss–Legendre_algorithm
# import decimal;decimal.getcontext().prec=11000;D=decimal.Decimal;a=p=1;b,t=1/D(2).sqrt(),1/D(4);[exec('z=(a+b)/2;t-=p*(a-z)**2;b=(a*b).sqrt();a=z;p*=2;pi=(z*2)**2/(4*t)',globals())for i in[1]*50];print(str(pi)[int(input())+2])

# Second method – multiple lines: 207 bytes
# Uses this algorithm: https://en.wikipedia.org/wiki/Gauss–Legendre_algorithm
import decimal;decimal.getcontext().prec=11000;D=decimal.Decimal;a=p=1;b,t=1/D(2).sqrt(),1/D(4)
for i in[1]*50:z=(a+b)/2;b=(a*b).sqrt();t-=p*(a-z)**2;a=z;p*=2;pi=(z*2)**2/(4*t)
print(str(pi)[int(input())+2])

# Third method – No "Decimal" module: FAIL
# a=p=1;b,t=1/(2**.5),1/4;q=10**10000;
# for i in[1]*50:z=(a+b)/2;b=(a*b)**.5;t-=p*(a-z)**2;a=z;p*=2;q+=(z*2)**2/(4*t)
# print(len(str(q)));print(str(q)[int(input())+2])

# Fourth Method – New algorithm:

