# This Challenge: http://codegolf.stackexchange.com/questions/85487/i-programming-puzzles-il-code-golf

# 243 bytes in Python 3.5.1
import re;a,b,c=eval(input());Q,K,L,R='le ',b=='m',c=='s',re.match;print([[[[Q,'i '][K],['la ','il '][K]][L],[[Q,'gli '][K],"l'"][L]][bool(R('[aeiou]',a))],[[Q,'gli '][K],['la ','lo '][K]][L]][bool(R('s[^aeiou]|(z|gn|pn|ps|x|i)[aeiou]',a))]+a)

# Second Version, 181 bytes (without the "F=" part)
import re;R=re.match;F=lambda a,b:(R('s[^aeiou]|(z|gn|pn|ps|x|i)[aeiou]',a)and['lo ','gli ','la '][b]or R('[aeiou]',a)and["l'",'gli ',"l'"][b]or['il ','i ','la '][b]if b<3else'le ')+a

# 235 bytes for first version in Python 2.7.10
# import re;a,b,c=input();Q,K,L,R='le ',b=='m',c=='s',re.match;print[[[[Q,'i '][K],['la ','il '][K]][L],[[Q,'gli '][K],"l'"][L]][bool(R('[aeiou]',a))],[[Q,'gli '][K],['la ','lo '][K]][L]][bool(R('s[^aeiou]|(z|gn|pn|ps|x|i)[aeiou]',a))]+a