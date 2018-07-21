# This Challenge: http://codegolf.stackexchange.com/questions/86753/make-a-sprite-sheet-from-all-the-stack-exchange-sites-favicons

from urllib.request import*;from PIL import Image as I;from io import*;import re
# print(re.sub('\s','',I)[2216:])
# print(I[:20000])
# print(I.index('<body>'))
# print(I[2978:])
# print(I.index('<div class="site-bubble"'))
# print(I[7167:])
H='http://';U=urlopen;u=y=0;V=sorted(re.findall('<h2><a href="%s((?!meta).+?.stackexchange.com)">'%H,U(H+'stackexchange.com/sites?view=list').read().decode()[7167:]))+['%s.com'%i for i in'stackexchange stackoverflow superuser serverfault askubuntu mathoverflow stackapps stackauth'.split()];i=I.new("RGBA",(320,-~(len(V)*2//10)*32))
for l in V+['meta.'+i for i in V]:
 try:
  i.paste(I.open(BytesIO(U(H+l+'/favicon.ico').read())),(u,y));u+=32
  if u>319:u=0;y+=32
 except:0
i.save('Collection8.png')