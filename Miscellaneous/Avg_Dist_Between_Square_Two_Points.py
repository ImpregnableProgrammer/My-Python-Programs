# Approx. avg distance between all pairs of points a square of side length a
def avgDist(a):
    totalDist = 0
    incrRatio = 100
    values = tuple(map(lambda i:i/incrRatio, range(a*incrRatio + 1)))
    for x1 in values:
        print(x1*100, end='% Done\n')
        for y1 in values:
            for x2 in values:
                for y2 in values:
                    totalDist += ((x1 - x2)**2 + (y1 - y2)**2)**.5 * (1/incrRatio)**4
        print("\x1b[A\33[2K\r", end='')
    return totalDist/(a**4)

from math import sin, cos, log
# Using Law of Cosines in Integral - NOT ANY SIMPLER TO EVALUATE SYMBOLICALLY THAN REGULAR INTEGRAL!!
def approxIntegral(a):
    Sum = 0
    pi = 3.1415
    incr = 1/100
    theta = 0
    while theta <= pi/2:
        theta2 = 0
        print(theta * 100 / (pi/2), end='% Done\n')
        while theta2 <= theta:
            r1 = 0
            r1_base = cos(theta) if theta <= pi/4 else sin(theta)
            r2_base = cos(theta2) if theta2 <= pi/4 else sin(theta2)
            while r1 <= a/r1_base:
                r2 = 0
                while r2 <= a/r2_base:
                    Sum += (r1**2 + r2**2 - 2*r1*r2*cos(theta - theta2))**.5 * r1 * r2 * (incr ** 4)
                    r2 += incr
                r1 += incr
            theta2 += incr
        theta += incr
        print("\33[A\33[2K\r", end='')
    return 2/(a**4) * Sum

a = 1
print("Approximation:", avgDist(a))
print("Approx Value using Lw of Cosines?:", approxIntegral(a))
print("Exact Value:", a/15 * (2**.5 + 2 + 5*log(2**.5 + 1)))

# Formula for exact value found by using mathod in following video: https://www.youtube.com/watch?v=i4VqXRRXi68
