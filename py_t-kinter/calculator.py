import tkinter as tk
from tkinter import *

v=tk.Tk()
v.geometry("500x500")
v.title("calculator")

def add():
    a=int(p1.get())
    b=int(p2.get())
    c=a+b
    p3.set("The addition is "+str(c))
    p1.set("")
    p2.set("")

def sub():
    a=int(p1.get())
    b=int(p2.get())
    c=a-b
    p3.set("The subtraction is "+str(c))
    p1.set("")
    p2.set("")

def mul():
    a=int(p1.get())
    b=int(p2.get())
    c=a*b
    p3.set("The multiplication is "+str(c))
    p1.set("")
    p2.set("")

def div():
    a=int(p1.get())
    b=int(p2.get())
    c=a/b
    p3.set("The division is "+str(c))
    p1.set("")
    p2.set("")

p1=StringVar()
p2=StringVar()
p3=StringVar()

lf=tk.Label(v,text="Enter first number:").grid(row=1,column=0)
tf=tk.Entry(v,textvariable=p1).grid(row=1,column=1)

ls=tk.Label(v,text="Enter second number:").grid(row=2,column=0)
ts=tk.Entry(v,textvariable=p2).grid(row=2,column=1)

btnadd=tk.Button(v,text="+",width="10",command=add).grid(row=3,column=0)

btnsub=tk.Button(v,text="-",width="10",command=sub).grid(row=3,column=1)

btnmul=tk.Button(v,text="*",width="10",command=mul).grid(row=3,column=2)

btndiv=tk.Button(v,text="/",width="10",command=div).grid(row=3,column=3)

lans=tk.Label(v,text="",textvariable=p3).grid(row=4,column=0)


