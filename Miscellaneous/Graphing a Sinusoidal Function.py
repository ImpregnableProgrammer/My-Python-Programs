import tkinter as tk
import re
from math import pi


class Sinusoidal(tk.Frame):

    def __init__(self,equation,master=None):
        super().__init__(master)
        self.pack()
        Information=re.split('\*?(?:cos|sin)\(|\*?x\+|\)\+',equation.replace('^','**').replace('π','pi'))
        # print(Information)
        for i in range(4):
            if re.fullmatch('.*\d+pi',Information[i]):
                # print('hi',Information[i])
                Information[i]='*'.join(re.sub('(?<=\d)+(?=pi)',' ',Information[i]).split(' '))
        # print(Information)
        self.equation = equation
        self.amplitude = eval(Information[0])
        self.period = eval(Information[1])
        self.shift = eval(Information[2])
        self.midline = eval(Information[3])
        self.Graph()

    def Graph(self):
        Canvas = tk.Canvas(self,height=1000,width=1000)
        Canvas.pack(expand=True,fill=tk.BOTH)
        Canvas.create_line(0,500,1000,500)
        Canvas.create_line(500,0,500,1000)
        for i in range(1,500,1):
            Canvas.create_line(i,499.5,i,500.5)
            Canvas.create_line(499.5,i,500.5,i)
            Canvas.create_text(i,501,text=str((-500)+i),font=("Purisa",8))
            Canvas.create_text(501,i,text=str(500-i),font=("Purisa",8))
        for i in range(501,1000,1):
            Canvas.create_line(i,499.5,i,500.5)
            Canvas.create_line(499.5,i,500.5,i)
            if i!=501:
                Canvas.create_text(i,501,text=str((-500)+i),font=("Purisa",8))
            Canvas.create_text(501,i,text=str(500-i),font=("Purisa",8))
        Stack=[]
        i=473.995
        while i<=525.995:
            try:
                if'sin'in self.equation:
                    # print('hi')
                    Stack.append((i,500-(self.amplitude*self.Sin(self.period*(i-500)+self.shift)+self.midline)))
                    # print(str(i-500),':',(self.amplitude*self.Sin(self.period*(i-500))+self.midline))
                else:
                    # print('hoi')
                    Stack.append((i,500-(self.amplitude*self.Cos(self.period*(i-500)+self.shift)+self.midline)))
            except:
                pass
            i+=0.005
        Canvas.create_line(*Stack)
        Canvas.scale("all",500,500,19.5,19.5)

    def Factorial(self,l):
        f=[1];[f.append(f[-1]*i)for i in range(1,l+1)];return f[-1]

    def Sin(self,p):
        Stack=[]
        p%=(pi*2)
        for n in range(100):
            Stack.append((((-1)**n)/self.Factorial(2*n+1))*(p**(2*n+1)))
        return sum(Stack)

    def Cos(self,p):
        Stack=[]
        p%=(pi*2)
        for n in range(101):
            Stack.append((((-1)**n)/self.Factorial(2*n))*(p**(2*n)))
        return sum(Stack)


if __name__ == '__main__':
    equation=input()
    root = tk.Tk()
    root.wm_title('Graph of Sinusoidal Function '+equation)
    app=Sinusoidal(equation,root)
    app.mainloop()