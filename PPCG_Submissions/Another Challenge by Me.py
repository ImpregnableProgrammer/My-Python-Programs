from tkinter import*
def G(o):
    root=Tk()
    C=Canvas(root,height=400,width=400)
    C.pack(fill=BOTH,expand=TRUE)
    for i in o:
        C.create_line(*i,i[0],0)
        C.create_line(*i,i[0],1000)
        C.create_line(*i,1000,i[1])
        C.create_line(*i,0,i[1])
    root.mainloop()

G([(50,60),(200,140),(280,320)])