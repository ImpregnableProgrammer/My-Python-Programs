import subprocess
import time
from math import*
def Grapher(a,t,Z,H,A=0,T=1):
    Q=A
    J=("["+"' ',"*t+"' '],")*t
    E=eval("["+J+("["+"' ',"*t+"' ']")+"]")
    if a:
        for y in range(A,Z+2):
            for i in range(A,y):
                try:
                    E[eval(H)][i]="*"
                except ZeroDivisionError:
                    E[t][i]="*"
            for x in E[::-1]:
                print(''.join(x))
            Q+=1
            i=y
            print(Q,'→',eval(H))
            time.sleep(T)
            subprocess.run("clear")
    else:
        for i in range(A,Z+1):
            try:
                E[eval(H)][i]="*"
            except ZeroDivisionError:
                E[t][i]="*"
            # print("Input %d"%(i),"\u2192",floor(eval(H)*100))
        for x in E[::-1]:
            print(''.join(x))

Grapher(1,151,20,'(i-10)**2',T=0.1)
