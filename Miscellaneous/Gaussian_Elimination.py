
# Implementation of Gauss-Jordan Elimination
# Equations given as arrays of coefficents and solution
# e.g. [2, 3, 4, 6] is 2x + 3y + 4z = 6

# Perform Gauss-Jordan elimination to solve linear system.
# The objective is to reduce the augmented matrix to reduced row-echelon form,
# which is obtained using the elementary row operations:
# interchange eqs, multiply eq by non-zero constant, or add multiple of one eq to another.
# Technique:
# 1. Rearrange rows so any zeroes are in convenient positions for next step (if possible)
# 2. Turn augmented matrix into lower triangular (all zeroes above diagonal)
# 3. Diagonalize matrix (make rest of entries not on main diagonal zero)
# 4. Multipy each row by reciprocal of remaining non-zero value in the row
# Also handles over and under-determined systems for any N x M augmented matrix
class Gaussian_Elimination:

    # If `fraction` is true, exact solutions returned as fractions in tuples
    # e.g. (3, 4) is 3/4, (-2, 5) is -2/5
    # Fraction inputs given in same form of tuples if `fraction` is true;
    # otherwise in normal form a/b, which is represented by decimals internally
    def __init__(self, eqs, fraction = True):
        self.fraction = fraction
        self.n = len(eqs)
        self.m = len(eqs[0]) - 1
        if self.n < self.m:
            eqs += [[0] * (self.m + 1)] * (self.m - self.n)
        if self.fraction:
            self.augm = [[(elem, 1) if type(elem) == int else elem for elem in row] for row in eqs]
        else:
            self.augm = eqs
        self.coeffs = [row[:-1] for row in self.augm]
        self.consts = [row[-1] for row in self.augm]
        if self.n > self.m:
            self.augm = self.augm[:self.m]
        self.Reduced = None
        self.Solution = None
        self.Steps = []

    #### BEGIN UNNEEDED ####
    
    # Check if augmented matrix in reduced row-echelon form,
    # where each (non-zero) row has leading 1, with all zeroes above and below each leading 1,
    # each subsequent row's leading 1 is further to the right,
    # and zero rows are at the bottom of matrix.
    # Throws `Index Error` if system has any row of all zero coeffs.
    def Reduced_Row_Echelon_Check(self):
        all_leading_ones = all([elem for elem in eq if elem!=0][0] == 1 for eq in self.coeffs)
        indices = [eq.index(1) for eq in self.coeffs]
        echelon_check = len(set(indices)) == len(indices) and sorted(indices) == indices
        if all_leading_ones and echelon_check:
            transpose_coeffs = self.Transpose(self.coeffs)
            reduced_check = all([elem for elem in transpose_coeffs[i] if elem != 0] == [1] for i in indices)
            if reduced_check:
                return True
        return False

    def Transpose(self, mat):
        return [[row[i] for row in mat] for i in range(len(mat[0]))]

    #### END UNNEEDED ####

    #### Helper funcs for rational/fractional arithmetic ####
    
    def gcd(self, m, n):
        if min(m, n) > 0:
            return self.gcd(min(m, n), max(m, n) % min(m, n))
        else:
            return max(m, n)

    def frac_reduce(self, a):
        GCD = self.gcd(*[abs(num) for num in a])
        n, d = (e // GCD for e in a)
        return ((-1) ** (n / d < 0) * abs(n), abs(d))
    
    def frac_add(self, a, b):
        return self.frac_reduce((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))

    def frac_sum(self, fracs):
        Sum = (0, 1)
        for frac in fracs:
            Sum = self.frac_add(Sum, frac)
        return Sum
    
    def frac_subtrct(self, a, b):
        return self.frac_reduce((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))

    def frac_mult(self, a, b):
        return self.frac_reduce((a[0] * b[0], a[1] * b[1]))

    def frac_divide(self, a, b):
        return self.frac_reduce((a[0] * b[1], a[1] * b[0]))

    #### End helper funcs ####
        
    def Lower_Triangular(self):
        augm = self.augm[:]
        for col in range(len(augm[0]) - 2, -1, -1):
            for row in range(col):
                if augm[row][col] == 0 or (self.fraction and augm[row][col][0] == 0):
                    continue
                elif augm[row + 1][col] == 0 or (self.fraction and augm[row + 1][col][0] == 0):
                    curr_row = augm[row]
                    augm[row] = augm[row + 1]
                    augm[row + 1] = curr_row
                    self.Steps.append("R%d <-> R%d" % (row + 1, row + 2)) 
                    continue
                if self.fraction:
                    multiplier = self.frac_divide(augm[row][col], augm[row + 1][col])
                    augm[row] = [self.frac_subtrct(*pair) for pair in zip(augm[row], [self.frac_mult(elem, multiplier) for elem in augm[row + 1]])]
                    self.Steps.append("R%d + (%d/%d)R%d -> R%d" % (row + 1, *multiplier, row + 2, row + 1))
                else:
                    multiplier = augm[row][col] / augm[row + 1][col]
                    augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[row + 1]])]
        return augm

    def Diagonalize(self):
        augm = self.Lower_Triangular()
        for col in range(len(augm[0]) - 1):
            for row in range(len(augm) - 1, col, -1):
                if augm[row][col] == 0 or (self.fraction and augm[row][col][0] == 0):
                    continue
                elif augm[col][col] == 0 or (self.fraction and augm[col][col][0] == 0):
                    new_row = col + 1
                    while (augm[new_row][col] == 0 or (self.fraction and augm[new_row][col][0] == 0)) and new_row < row:
                        new_row += 1
                    if self.fraction:
                        multiplier = self.frac_divide(augm[row][col], augm[new_row][col])
                        augm[row] = [self.frac_subtrct(*pair) for pair in zip(augm[row], [self.frac_mult(elem, multiplier) for elem in augm[new_row]])]
                        self.Steps.append("R%d + (%d/%d)R%d -> R%d" % (row + 1, *multiplier, new_row + 1, row + 1))
                    else:
                        multiplier = augm[row][col] / augm[new_row][col]
                        augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[new_row]])]
                    continue
                if self.fraction:
                    multiplier = self.frac_divide(augm[row][col], augm[col][col])
                    augm[row] = [self.frac_subtrct(*pair) for pair in zip(augm[row], [self.frac_mult(elem, multiplier) for elem in augm[col]])]
                    self.Steps.append("R%d + (%d/%d)R%d -> R%d" % (row + 1, *multiplier, col + 1, row + 1))
                else:
                    multiplier = augm[row][col] / augm[col][col]
                    augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[col]])]
        return augm

    def Solve(self):
        augm = self.Diagonalize()
        for row in range(len(augm)):
            if augm[row][row] == 0 or (self.fraction and augm[row][row][0] == 0):
                if augm[row][-1] == 0 or (self.fraction and augm[row][-1][0] == 0):
                    self.Solution = False
                    return "Infinite Solutions!"
                return "No Solution!"
            if self.fraction:
                self.Steps.append("(%d/%d)R%d" % (*self.frac_reduce(augm[row][row][::-1]), row + 1))
                augm[row] = [self.frac_divide(elem, augm[row][row]) for elem in augm[row]]
            else:
                augm[row] = [elem / augm[row][row] for elem in augm[row]]
        self.Reduced = augm
        self.Solution = [row[-1] for row in augm]
        if self.Verify():
            return self.Solution
        else:
            return "No Solution!"

    # Only call after solving system to verify solution
    def Verify(self):
        if not self.Solution:
            return "Solve the system first!"
        if self.fraction:
            sub = [self.frac_sum([self.frac_mult(a,x) for a,x in zip(row, self.Solution)]) for row in self.coeffs]
        else:
            sub = [round(sum([a*x for a,x in zip(row, self.Solution)])) for row in self.coeffs]
        return sub == self.consts

    # Only call after solving system to get steps taken
    # Steps only given for fraction mode, since they're messy in decimal mode
    def getSteps(self):
        if not self.fraction:
            print("Steps only given for fraction mode!")
        elif self.Solution == None:
            print("Solve the system first!")
        else:
            for i in range(len(self.Steps)):
                print("%d. %s" % (i+1, self.Steps[i]))

                
if __name__ == "__main__":

    # Test it out!

    # 2x2 coeff matrix
    '''Eqs = [[4, 5, 8],
           [7, 5, 13]]'''
    
    # 3x3 coeff matrix
    '''Eqs = [[5,8,4,1],
           [2,6,3,3],
           [7,9,2,9]]'''
    
    # 4x4 coeff matrix
    '''Eqs = [[5, 3, 6, 9, 0],
           [2, 1, 5, 7, 0],
           [0, 3, 1, 0, 9],
           [0, 9, 0, 1, 0]]'''

    # With fractions
    Eqs = [[1, (2, 5), -3, -2],
           [3, 1, (-1, 4), 5],
           [2, 2, 1, 4]]

    # With decimals; switch to non-fraction mode
    # Pass `False` as second argument during instantiation
    '''Eqs = [[1, 2/5, -3, -2],
           [3, 1, -.25, 5],
           [2, 2, 1, 4]]'''

    # Overdetermined system
    '''Eqs = [[1, (2, 5), -3],
           [3, 1, (-1, 4)],
           [6, 5, (-1, 2)]]'''

    # Underdetermined system
    '''Eqs = [[1, 9, 7, 6],
           [5, 7, 3, 8]]'''
    
    Process = Gaussian_Elimination(Eqs)
    print("Augmented Matrix:", Process.augm)
    print("Lower Triangular:", Process.Lower_Triangular())
    print("Diagonalized:", Process.Diagonalize())
    print("Solution (pay attention to the signs!):", Process.Solve())
    print("Reduced matrix:", Process.Reduced)
    print("Steps (pay attention to the signs!):")
    Process.getSteps()
