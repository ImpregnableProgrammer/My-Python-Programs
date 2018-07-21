# This Challenge: http://codegolf.stackexchange.com/questions/85141/draw-the-national-flag-of-iceland

# 235 bytes
from tkinter import*;C=Canvas(Tk(),height=126,width=175,bg='#d72828');C.pack();X=lambda*a:C.create_rectangle(a,fill='#0048E0',outline='#fff',width=7);X(0,0,8,8);X(0,11,8,19);X(11,0,26,8);X(11,11,26,19);C.scale('all',0,0,7,7);mainloop()