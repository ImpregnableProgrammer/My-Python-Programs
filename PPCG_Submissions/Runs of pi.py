# This Challenge: http://codegolf.stackexchange.com/questions/85388/runs-of-digits-in-pi

# Using urllib to fetch 1000000 digits of pi from website
from urllib.request import*;import re;
def R():
 Y=urlopen('http://www.walloftvs.org/resources/v1/pi.html').read().decode()
 Q=re.findall('3\.\d+\d+',''.join(re.split('\s',Y)))[0];i=0
 while re.search(r'(\d)\1{%s}?'%i,Q):print(re.search(r'(\d)\1{%s}?'%i,Q));i+=1

# Calculating pi up to input number of digits and find numbers of sequence in first n digits of pi
# Input = 10000 (ten thousand) takes about 4 seconds to complete
# Input = 100000 (one hundred thousand) takes about 54 sec. to complete
# Input = 1000000 (one million) takes about 12 min. 24 sec. to complete
# Input = 6000000 (six million) takes about 2 hrs. 26 min. to complete
# 263 bytes (without the calls to time() and the time() import)
import decimal,re,time;P=time.time();decimal.getcontext().prec=int(input());D=decimal.Decimal;a=p=1;b,t=1/D(2).sqrt(),1/D(4);f=0
for i in[1]*50:z=(a+b)/2;b=(a*b).sqrt();t-=p*(a-z)**2;a=z;p*=2;f+=1;print(f)
pi=(a+b)**2/(4*t);g=0;C=lambda r:re.search(r'(\d)\1{%s}'%r,str(pi))
while C(g):print(C(g));g+=1
print(time.time()-P)

# Input = 10000000 (ten million) finished in about 4 hrs. 20 min. after which the following was output:
# <_sre.SRE_Match object; span=(0, 1), match='3'>
# <_sre.SRE_Match object; span=(25, 27), match='33'>
# <_sre.SRE_Match object; span=(154, 157), match='111'>
# <_sre.SRE_Match object; span=(763, 767), match='9999'>
# <_sre.SRE_Match object; span=(763, 768), match='99999'>
# <_sre.SRE_Match object; span=(763, 769), match='999999'>
# <_sre.SRE_Match object; span=(710101, 710108), match='3333333'>
