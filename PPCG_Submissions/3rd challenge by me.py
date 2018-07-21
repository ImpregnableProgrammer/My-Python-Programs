from tkinter import*
def G(o):
    root=Tk()
    h = 500
    C=Canvas(root,height=h,width=h)
    C.pack(fill=BOTH,expand=TRUE)
    for u in o:
        # M=[]
        # for x in[-250,250]:
        #     y=eval(u[2:].replace('x','*x'))
        #     print(y)
        #     M+=[x,y]
        if u[0]=='y':
            C.create_line(-(h/2),(h/2)-int(u[2:]),h,(h/2)-int(u[2:]))
        else:
            C.create_line((h/2)+int(u[2:]),-(h/2),(h/2)+int(u[2:]),h)
    root.mainloop()

G(['x=0','x=81','x=90','y=0','y=90','y=100'])

# def G(o):
#     root=Tk()
#     C=Canvas(root,height=500,width=500)
#     C.pack(fill=BOTH, expand=TRUE)
#     for i in o:
#         C.create_line(250+i[0],250-i[1],250+i[2],250-i[3])
#         C.create_text((250+i[2])//2,(250-i[3])//2,text=str(int(((i[2]-i[0])**2+(i[3]-i[1])**2)**.5)))
#     root.mainloop()
#
# G([(40,100,80,100)])