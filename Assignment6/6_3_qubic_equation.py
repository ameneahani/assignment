from math import *

def qubic_equa():
    p=round((b-a**2/3),2)
    q=round((2*a**3/27-a*b/3+c),2)
    Δ=round((q**2/4+p**3/27),2)
    print("p=",p,"q=",q)
    print("Δ=", Δ)
    if Δ>0:
        x=(-q/2+sqrt(Δ))**(1/3)+(-q/2+sqrt(Δ))**(1/3)-a/3
        print (x)

    if Δ==0:
        x1=-2*(q/2)**(1/3)-a/3
        x2=(q/2)**(1/3)-a/3
        print("x1= ",x1,"x2=x3= ",x2)

    if Δ<0:
        e1=(2/sqrt(3))*sqrt(-p)
        e2=(1/3)*(1/sin((3*sqrt(3)*q)/(2*sqrt(-p)**3)))
        x1=e1*sin(e2)-a/3
        x2=-e1*sin(e2+pi/3)-a/3
        x3=e1*cos(e2+pi/6)-a/3
        print("x1= ",x1,"x2= ",x2,"x3= ",x3)

num1=0
while num1==0:
    num1=int(input("a = "))
    if num1==0:
        print("a cant be zero please try again")
a=int(input("b = "))/num1
b=int(input("c = "))/num1
c=int(input("d = "))/num1
qubic_equa(a,b,c)
