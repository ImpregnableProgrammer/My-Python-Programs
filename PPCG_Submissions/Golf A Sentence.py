# This Challenge: http://codegolf.stackexchange.com/questions/84966/golf-a-sentence

import re;R=re.sub;W=lambda G:G.group(0);print(R(r'(\W)\1+',lambda f:W(f)[0],R('\s*[^\s\w]\s*|\s*[A-Z]',lambda f:W(f).strip(),R('((I|i)t|(s|S)?(h|H)e) is',lambda i:W(i)[:[*W(i)].index(" ")]+"'s",input().strip()))))