# This Challenge: http://codegolf.stackexchange.com/questions/86976/draw-a-fibonacci-network

# Used to generate Fibonacci Sequence shown here: http://oeis.org/A000045
from tkinter import*
root=Tk()
C=Canvas(root,height=1000,width=1000)
C.pack(fill=BOTH,expand=True)
x=y=5
Y=lambda i:0if i==0else 1if i==1else Y(i-1)+Y(i-2)
for i in range(1,int(input())+1):
    for j in range(Y(i)):
        C.create_oval(x,y,x+10,y+10)
        x+=30
    y+=30
    x=5
    # print('* '*Y(i)+'\n'+'|\\'[:i]*Y(i))
root.mainloop()