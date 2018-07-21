# This Challenge: http://codegolf.stackexchange.com/questions/87051/is-the-dag-a-transitive-reduction

# Visualize Test Cases
from random import*
def R(o):
    import tkinter as tk
    root=tk.Tk()
    C=tk.Canvas(root,height=1000,width=1000)
    C.pack(fill=tk.BOTH,expand=True)
    U={y:u for y,u in zip(range(len(o)+1),o)}
    Q=[];B=[]
    for i in list(U.keys())[1:]:
        # def J():C=randint(5,950);return C if all(i not in Q for i in range(C,C+250))and all(i not in B for i in range(C,C+250))else J()
        # n,m=J(),J()
        C.create_oval(n,m,n+20,m+20,tag=str(i))
        C.create_text(n+10,m+10,text=chr(65+i))
        # Q.append(C.coords(str(i))[0])
        # B.append(C.coords(str(i))[1])
        # if n>=0 and m<500:
        #     n+=50;m+=a
        # elif n>=0 and m>=500:
        #     n-=50;m+=a
        # a+=25
    for i in list(U.keys())[1:4]:
        for e in U[i]:
            F,S=C.coords(str(i)),C.coords(str(e))
            print(F)
            print(F[0],F[1],S[0],S[1])
            C.create_line(F[0],F[1],S[0],S[1])
    root.mainloop()


R([[1,2],[3],[3],[]])