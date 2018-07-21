
# Width of bottom inner rectangle = 0.817
# Height of bottom inner rectangle = 0.263
# 1) 0.1745
# 2)
from tkinter import*
root=Tk()
C=Canvas(root,height=500,width=500)
C.pack(fill=BOTH,expand=True)
C.create_oval(249,249,251,250.9,fill='black')
# C.update()
# print(C.winfo_height(),C.winfo_width())
# C.create_arc(249.085,249.085,105,100,start=180,extent=-180,fill='white',width=0)
C.create_rectangle(249.817,249.8255,250.183,250.1745,fill='white',width=0)
# C.create_arc(4,4,9,9,start=180,extent=180,style=ARC,fill='black',width=4)
# C.create_rectangle(1.268,1.2595,1.902,1.7605,fill='white',width=0)
# C.create_rectangle(0.817,)
C.scale('all',250,250,100,100)
root.mainloop()
