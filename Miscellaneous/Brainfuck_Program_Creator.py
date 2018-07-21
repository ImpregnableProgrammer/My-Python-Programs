# Creates a Brainfuck program that outputs some input string; NOT *FULLY* optimal (yet...); Recursive solution
E=lambda c,j=[],l='':len(c)>0 and E(c[1:],j+[min(''.join(min([(sum([ord(c[0])/j,j]),'>'+'+'*(abs(ord(l or'\x00')-ord(c[0]))//j)+'['+'<'+'-+'[l==''or l<c[0]]*j+'>-]<.')for j in range(1,-~abs(ord(l or'\x00')-ord(c[0])))if abs(ord(l or'\x00')-ord(c[0]))/j==abs(ord(l or'\x00')-ord(c[0]))//j]or[(0,'.')],key=lambda g:g[0])[1:]),'-+'[ord(l or'\x00')<ord(c[0])]*(abs(ord(l or'\x00')-ord(c[0])))+'.',key=len)],c[0])or''.join(j)


