import tkinter as tk
from tkinter import *

p=tk.Tk()
p.geometry("500x500")
p.title("Simple Intrest")

def si():
    a=int(v1.get())
    b=int(v2.get())
    c=int(v3.get())
    d=(a*b*c)/100
    v4.set("Your simple intrest is "+str(d))
    
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

lp=tk.Label(p,text="Enter prise:").grid(row=0,column=0)
tp=tk.Entry(p,textvariable=v1).grid(row=0,column=1)

lr=tk.Label(p,text="Enter ret of intrest:").grid(row=1,column=0)
tr=tk.Entry(p,textvariable=v2).grid(row=1,column=1)

ln=tk.Label(p,text="Enter Time:").grid(row=2,column=0)
tn=tk.Entry(p,textvariable=v3).grid(row=2,column=1)

btnsi=tk.Button(p,text="SI",width="10",command=si).grid(row=3,column=1)

lans=tk.Label(p,text="",textvariable=v4).grid(row=4,column=1)
