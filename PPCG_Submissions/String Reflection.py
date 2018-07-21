# This Challenge:

# Assumes Rectangular Input:
# Version 1 - Lambda: 61 bytes
J=lambda f,j:[print(r[::-1])for r in j[::[1,-1][f]].split('\n')]
# Version 2 - Function:  bytes
def J(f,j):[print(r[::-1])for r in j[::[1,-1][f]].split('\n')]

# Does not assume rectangular input: 133 bytes
# Version 1 - Function: 129 bytes
def J(f,j):print('\n'.join([' '*((max([len(i)for i in j.split('\n')])-len(r))*(not f))+r[::-1]for r in j[::[1,-1][f]].split('\n')]))
# Version 2 - Lambda: 129 bytes
J=lambda f,j:print('\n'.join([' '*((max([len(i)for i in j.split('\n')])-len(r))*(not f))+r[::-1]for r in j[::[1,-1][f]].split('\n')]))