##################
# The challenge: ####################################################################################################
#   http://codegolf.stackexchange.com/questions/80904/my-keybore-is-key-boring-me-help-me-find-a-minimal-keystrokes #
#####################################################################################################################

def R(j):
    import re,random;h=lambda j:sum([(len(i)*(len(i)+1))/2if i[-1]=='+'else-((len(i)*(len(i)+1))/2)for i in re.sub('(?<=(-))(?=(\+))|(?<=(\+))(?=(-))',' ',j).split()])
    k=[]
    for i in range(2):
        m=['-+'[i==1]]
        while h(''.join(m))!=j:
            if h(''.join(m))<j:
                m.append('+')
            elif h(''.join(m))>j:
                m.append('-')
        k.append(''.join(m))
    return len(''.join(min(k,key=len)))

# [print(R(i))for i in range(51)]
print(R(361))

# Another Version
def R2(j):
    import re;h=lambda j:sum([(len(i)*(len(i)+1))/2if i[-1]=='+'else-((len(i)*(len(i)+1))/2)for i in re.sub('(?<=(-))(?=(\+))|(?<=(\+))(?=(-))',' ',j).split()])
    m=[]
    while h(''.join(m))!=j:
        if h(''.join(m))<j:
            m.append('+')
        elif h(''.join(m))>j:
            m.append('-')
    w=[]
    for i in range(len(''.join(m))):
        k=['+']*i
        print(k)
        while h(''.join(k))!=j:
            if h(''.join(k))<j:
                k.append('+')
            elif h(''.join(k))>j:
                k.append('-')
        w.append(''.join(k))
        print(w)
    return''.join(min(w,key=len))

# print(R2(97)) #

# Another Version; This one uses a cartesian product method and therefore is INCREDIBLY slow
import itertools,re
def R3(j):
    z=[];h=lambda j:sum([(len(i)*(len(i)+1))/2if i[-1]=='+'else-((len(i)*(len(i)+1))/2)for i in re.sub('(?<=(-))(?=(\+))|(?<=(\+))(?=(-))',' ',j).split()])
    for i in range(1,j+1):
        e=itertools.product(['+','-'],repeat=i)
        [z.append(i)for i in itertools.product(['+','-'],repeat=i)if h(''.join(i))==j]
    return''.join(min(z,key=len))

# print(R3(361)) #

# Yet Another Version
def R4(j):
    import re,random;h=lambda j:sum([(len(i)*(len(i)+1))/2if i[-1]=='+'else-((len(i)*(len(i)+1))/2)for i in re.sub('(?<=(-))(?=(\+))|(?<=(\+))(?=(-))',' ',j).split()])
    k=[]
    for i in range(2):
        m=['-+'[i==1]]
        while h(''.join(m))!=j:
            m.append(random.choice(['+','-']))
        k.append(''.join(m))
    return''.join(min(k,key=len))

# print(R4(361)) #

# ANY even number can apparently be represented by a repetition of many `++-`s, followed by a `+` for ANY odd number.
# Try it now!
def R5(j):
    import re;h=lambda j:sum([(len(i)*(len(i)+1))/2if i[-1]=='+'else-((len(i)*(len(i)+1))/2)for i in re.sub('(?<=(-))(?=(\+))|(?<=(\+))(?=(-))',' ',j).split()])
    m=[]
    for g in range(j+1):
        while h(''.join(m))!=g:
            if h(''.join(m))<g:
                m.append('+')
            elif h(''.join(m))>g:
                m.append('-')
    return''.join(m)