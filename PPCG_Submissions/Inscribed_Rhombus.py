# This Challenge: http://codegolf.stackexchange.com/questions/100327/i-really-wanted-a-rhombus-but-all-i-got-was-this-stupid-rectangle/100349#100349

# Ungolfed - Without Color AND Without Top+Bottom lines of Rhombus
from tkinter import*
def V(a,b):S=500;Diag=(a**2+b**2)**0.5;D=Tk();C=Canvas(D);C.create_oval(S+Diag,S-Diag,S-Diag,S+Diag);C.create_oval((S+a)-Diag,(S-b)+Diag,(S+a)+Diag,(S-b)-Diag);C.create_line(S+a,S-b,S,S);C.create_rectangle(S+a,S,S,S-b);Slope=-(((S-b)-S)/((S+a)-S))**-1;Point=(Diag,(Diag)*Slope);C.create_line((((S+a)+S)/2)+Point[0],(((S-b)+S)/2)+Point[1],(((S+a)+S)/2)-Point[0],(((S-b)+S)/2)-Point[1]);Point2=(a>b)and((((S-b)-(((S-b)+S)/2))/Slope)+(((S+a)+S)/2),(S-b))or ((S+a),Slope*((S+a)-(((S+a)+S)/2))+(((S-b)+S)/2));Point3=(a>b)and(((S-(((S-b)+S)/2))/Slope)+(((S+a)+S)/2),S)or (S,Slope*(S-(((S+a)+S)/2))+(((S-b)+S)/2));C.create_line(S,S,Point2[0],Point2[1]);C.create_line(S+a,S-b,Point3[0],Point3[1]);C.pack(fill='both',expand=1)

# Golfed - Without Color but With Top+Bottom Lines of Rhombus
from tkinter import*
def V(a,b):S=500;Y,Z=S+a,S-b;M=(a**2+b**2)**0.5;D=Tk();C=Canvas(D);B=C.create_oval;X=C.create_line;B(S+M,S-M,S-M,S+M);B(Y-M,Z+M,Y+M,Z-M);X(Y,Z,S,S);C.create_rectangle(Y,S,S,Z);Q=-((Z-S)/(Y-S))**-1;U,V=(Y+S)/2,(Z+S)/2;X(U+M,V+M*Q,U-M,V-M*Q);P=[(Y,Q*(Y-U)+V),(((Z-V)/Q)+U,Z)][a>b];L=[(S,Q*(S-U)+V),(((S-V)/Q)+U,S)][a>b];X(S,S,P[0],P[1]);X(Y,Z,P[0],P[1]);X(Y,Z,L[0],L[1]);X(S,S,L[0],L[1]);C.pack(fill=BOTH,expand=1)

# Golfed - With Color and With Top+Bottom Lines of Rhombus 
from tkinter import*
def V(a,b):S=500;t='blue';Y,Z=S+a,S-b;M=(a**2+b**2)**0.5;D=Tk();C=Canvas(D);B=C.create_oval;X=C.create_line;B(S+M,S-M,S-M,S+M,outline=t);B(Y-M,Z+M,Y+M,Z-M,outline=t);X(Y,Z,S,S,fill=t);C.create_rectangle(Y,S,S,Z);Q=-((Z-S)/(Y-S))**-1;U,V=(Y+S)/2,(Z+S)/2;X(U+M,V+M*Q,U-M,V-M*Q,fill=t);P=[(Y,Q*(Y-U)+V),(((Z-V)/Q)+U,Z)][a>b];L=[(S,Q*(S-U)+V),(((S-V)/Q)+U,S)][a>b];o='orange';X(S,S,P[0],P[1],fill=o);X(Y,Z,P[0],P[1],fill=o);X(Y,Z,L[0],L[1],fill=o);X(S,S,L[0],L[1],fill=o);C.pack(fill=BOTH,expand=1)
