# This Challenge:

# First Version, in a Single Line; 467 bytes
# o=input();E=exec;R=range;a=dict(zip([*",./;'[]\\-=`1234567890",*map(chr,R(97,123))],[*'<>?:"{}|+_~!@#$%^&*()',*map(chr,R(65,91))]));b,c=[],'';C=S=0;G={'<del>':'b.pop()','<caps>':'C=[1,0][C==1]','<shft>':'S=1','<spc>':'b+=" "','<tab>':'b+=" "*4','<ret>':'b+="\n"'};N=lambda h:E('c="";'+G[h],globals())if h in G.keys()else E('');[E([[['b+=i','b+=i.upper()'][C>0],'b+=a[i];S=0'][S>0],'c+=i;N(c)'][i=='<'or len(c)>0],locals(),globals())for i in o.lower()];print(''.join(b))

# Second Version, in multiple lines; 433 bytes
o=input();E=exec;R=range;a=dict(zip([*",./;'[]\\-=`1234567890"],[*'<>?:"{}|+_~!@#$%^&*()']));b,c=[],'';C=S=0;G={'<del>':'b=b[:-1]','<caps>':'C=[1,0][C>0]','<shft>':'S=1','<spc>':'b+=" "','<tab>':'b+=" "*4','<ret>':'b+="\\n"'};N=lambda h:E('c="";'+G[h],globals())if h in G.keys()else E('')
for i in o.lower():E([[['b+=i','b+=i.upper()'][C>0],'b+=a[i]if i in a else i.upper();S=0'][S>0],'c+=i;N(c)'][(i=='<')+len(c)>0])
print(''.join(b))

# import re;a=dict(zip([*",./;'[]\\-=`1234567890"],[*'<>?:"{}|+_~!@#$%^&*()']));o=re.findall('<shft>(?:\w|\d){1}|<spc>|<caps>.+(?:<caps>)|<tab>|<ret>|\w*',input().lower());print(o)

# import re;print(re.sub('.*<del>','',input().lower()))

# Third Version: FAIL
# import re;R=range;a=dict(zip([*",./;'[]\\-=`1234567890",*map(chr,R(97,123))],[*'<>?:"{}|+_~!@#$%^&*()',*map(chr,R(65,91))]));p=input();o=re.sub('<caps>.+',lambda h:h.group(0)[6:].upper(),re.sub('<shft>(?:\w|\d){1}',lambda k:a[k.group(0)[-1]],re.sub('<spc>|<tab>|<ret>',lambda i:[['\n',' '*4][i.group(0)=='<tab>'],' '][i.group(0)=='<spc>'],re.sub('.*<del>','',p.lower()))));print(repr(o))
# o=re.sub('<shft>(?:\w|\d){1}|<caps>.+?(?=<caps>)|<spc>|<tab>|<ret>|\w*',lambda i:' 'if i.group(0)=='<spc>'else' '*4if i.group(0)=='<tab>'else'\n'if i.group(0)=='<ret>'else a[i.group(0)[-1]]if i.group(0)[:6]=='<shft>'else i.group(0)[6:].upper()if i.group(0)[:6]=='<caps>'else i.group(0),input().lower());print(o)

# Third Version, Regular Expressions: 652 bytes
# import re;a=dict(zip([*",./;'[]\\-=`1234567890",*map(chr,R(97,123))],[*'<>?:"{}|+_~!@#$%^&*()',*map(chr,R(65,91))]));print(re.sub('(<del>)?(?:<ret>|<spc>|<tab>|.)<del>|<(?:TAB|tab)>|<(?:SHFT|shft)>.|<(?:SPC|spc)>|<(?:RET|ret)>|\w*',lambda i:' 'if i.group(0)=='<SPC>'or i.group(0)=='<spc>'else' '*4if i.group(0)=='<TAB>'or i.group(0)=='<tab>'else'\n'if i.group(0)=='<RET>'or i.group(0)=='<ret>'else a[i.group(0)[-1]]if i.group(0)[:6]=='<shft>'or i.group(0)[:6]=='<SHFT>'else''if'<del>'in i.group(0)else i.group(0),re.sub(r'<caps>.+<caps>|<caps>.+',lambda i:i.group(0)[6:-6].upper()if i.group(0)[-6:]=='<caps>'else i.group(0)[6:].upper(),input().lower())))

# print(input().lower())
import re
print(re.sub('(<del>)?(?:<ret>|<spc>|<tab>|.)*(?:<del>)+',lambda h:''.join([*re.findall('\w+',re.sub('<ret><del>','',h.group(0)))[0]][:-(h.group(0).count('<del>'))]),input().lower()))
# (?:<(?:RET|ret|SPC|spc|TAB|tab.)>|.)

# Reverse of above method: 526 bytes
import re;a=dict(zip([*",./;'[]\\-=`1234567890",*map(chr,R(97,123))],[*'<>?:"{}|+_~!@#$%^&*()',*map(chr,R(65,91))]));print(re.sub(r'<caps>.+<caps>|<caps>.+',lambda i:i.group(0)[6:-6].upper()if i.group(0)[-6:]=='<caps>'else i.group(0)[6:].upper(),re.sub('(<del>)?(?:<ret>|<spc>|<tab>|.)<del>|<tab>|<shft>.|<spc>|<ret>|\w*',lambda i:' 'if i.group(0)=='<spc>'else' '*4if i.group(0)=='<tab>'else'\n'if i.group(0)=='<ret>'else a[i.group(0)[-1]]if i.group(0)[:6]=='<shft>'else''if'<del>'in i.group(0)else i.group(0),input().lower())))

# Even more golfed version of above method: 490 bytes
import re;a=dict(zip([*",./;'[]\\-=`1234567890",*map(chr,R(97,123))],[*'<>?:"{}|+_~!@#$%^&*()',*map(chr,R(65,91))]));U=lambda i:i.group(0);print(re.sub('<caps>(?:\s|.)+<caps>|<caps>(?:\s|.)+',lambda i:[U(i)[6:].upper(),U(i)[6:-6].upper()][U(i)[-6:]=='<caps>'],re.sub('(<del>)?(?:<ret>|<spc>|<tab>|.)+(?:<del>)+|<tab>|<shft>.|<spc>|<ret>|\w*',lambda i:[[[[U(i),'']['<del>'in U(i)],'\n'][U(i)=='<ret>'],' '*4][U(i)=='<tab>'],' '][U(i)=='<spc>']if U(i)[:6]!='<shft>'else a[U(i)[-1]],input().lower())))