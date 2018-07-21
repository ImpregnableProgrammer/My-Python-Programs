# The Website: http://cryptopals.com

# The First Challenge: Convert from Hex to Base64
# More about Base64: https://en.wikipedia.org/wiki/Base64
def w2(m):
 n=sum([(ord(g)-55)*h if not g.isdigit()else int(g)*h for g,h in zip(list(m.upper()),[16**e for e in range(0,len(m))][::-1])])
 p=[]
 z={i:g for i,g in enumerate([*map(chr,range(65,91)),*map(chr,range(97,123)),*map(str,range(10)),*'+/'])}
 while 1:
  p.append(z[n%64]);n=n//64
  if n<1:break
 print(''.join(p[::-1]))

print(w2('0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3721'))

# The Second Challenge: Fixed XOR
# More about Python's Bitwise operators: https://wiki.python.org/moin/BitwiseOperators
def T(p):
    return hex(int(p, 16) ^ int('686974207468652062756c6c277320657965', 16))

print(T('0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3721'))


