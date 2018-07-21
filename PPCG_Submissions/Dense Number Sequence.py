# This Challenge: http://codegolf.stackexchange.com/questions/89943/dense-number-sequence
G=lambda i:all(i%g!=0for g in range(2,i))
print([i for i in range(2,201)if G(i)or len({j for j in range(2,i)if i%j<1and G(j)and G(i//j)})>1])