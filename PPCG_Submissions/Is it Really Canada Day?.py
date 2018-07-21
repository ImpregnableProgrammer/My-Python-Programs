# This Challenge: http://codegolf.stackexchange.com/q/84510/52405
from urllib.request import*
H=lambda i:urlopen('http://enwp.org/'+i).read().count(b"Canada")

print(H('July_1'))