
# Implementation of Gauss-Jordan Elimination
# Equations given as arrays of coefficents and solution
# e.g. [2, 3, 4, 6] is 2x + 3y + 4z = 6

# Perform Gauss-Jordan elimination to solve system.
# The objective is to reduce the augmented matrix to reduced row-echelon form,
# which is obtained using the elementary row operations:
# interchange eqs, multiply eq by non-zero constant, or add multiple of one eq to another.
# Technique:
# 1. Rearrange rows so any zeroes are in convenient positions for next step (if possible)
# 2. Turn augmented matrix into lower triangular (all zeroes above diagonal)
# 3. Diagonalize matrix (make rest of entries not on main diagonal zero)
# 4. Multipy each row by reciprocal of remaining non-zero value in the row
class Gaussian_Elimination:
    
    def __init__(self, eqs):
        self.coeffs = [eq[:-1] for eq in eqs]
        self.consts = [eq[-1] for eq in eqs]
        self.augm = eqs

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

    def Lower_Triangular(self):
        augm = self.augm[:]
        for col in range(len(augm[0]) - 2, -1, -1):
            for row in range(col):
                if augm[row][col] == 0:
                    continue
                elif augm[row + 1][col] == 0:
                    curr_row = augm[row]
                    augm[row] = augm[row + 1]
                    augm[row + 1] = curr_row
                    continue
                multiplier = augm[row][col] / augm[row + 1][col]
                augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[row + 1]])]
        return augm

    def Diagonalize(self):
        augm = self.Lower_Triangular()
        for col in range(len(augm[0]) - 1):
            for row in range(len(augm) - 1, col, -1):
                if augm[row][col] == 0:
                    continue
                elif augm[col][col] == 0:
                    new_row = col + 1
                    while augm[new_row][col] == 0 and new_row < row:
                        new_row += 1
                    multiplier = augm[row][col] / augm[new_row][col]
                    augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[new_row]])]
                    continue
                multiplier = augm[row][col] / augm[col][col]
                augm[row] = [sum(pair) for pair in zip(augm[row], [-elem * multiplier for elem in augm[col]])]
        return augm

    def Solve(self):
        augm = self.Diagonalize()
        for row in range(len(augm)):
            if augm[row][row] == 0:
                if augm[row][-1] != 0:
                    return "No Solution!"
                return "Infinite Solutions!"
            augm[row] = [elem / augm[row][row] for elem in augm[row]]
        self.Reduced = augm
        self.Solution = [row[-1] for row in augm]
        return self.Solution, self.Verify()

    def Verify(self):
        return [round(sum([a*x for a,x in zip(row, self.Solution)])) for row in self.coeffs] == self.consts

Eqs = [[5, 3, 6, 9, 0],
       [2, 1, 5, 7, 0],
       [0, 3, 1, 0, 9],
       [0, 9, 0, 1, 0]]

'''Eqs = [[4, 3, 5, 7],
       [3, 0, 6, 8],
       [2, 6, 9, 2]]'''

Process = Gaussian_Elimination(Eqs)
print("Lower Triangular:", Process.Lower_Triangular())
print("Diagonalized:", Process.Diagonalize())
print("Solution:", Process.Solve())
