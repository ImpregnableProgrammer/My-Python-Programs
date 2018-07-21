#####################################
# More About Binary Searching Here: ###############################################################
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search #
###################################################################################################

def BinarySearch(z,l,g):
    y=[*range(l,g+1)]
    mini=0
    maxi=len(y)
    while y[(mini+maxi)//2]!=z:
         if y[(mini+maxi)//2]>z:
             maxi=((mini+maxi)//2)-1
         elif y[(mini+maxi)//2]<z:
             mini=((mini+maxi)//2)+1
    print('Index',(mini+maxi)//2,'=',z)

BinarySearch(56,1,20)