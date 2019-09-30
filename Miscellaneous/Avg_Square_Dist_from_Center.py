import math, sys
def avgDist(a):
    # Side length a
    totalDist = 0
    incr_ratio = 1000
    for x in range(0, a * incr_ratio):
        for y in range(0, a * incr_ratio):
            # Add D*dx*dy (where D is distance from center (.5,.5)) to total_dist
            totalDist += (((x/incr_ratio - a/2)**2 + (y/incr_ratio - a/2)**2)**.5) * (1 / incr_ratio) ** 2
    return totalDist / a**2

a = int(sys.argv[1])
print("Numerical Approximation:",avgDist(a))
print("Definite Integration result:",a / 6 * (2**.5 + math.log(2**.5 + 1)))
