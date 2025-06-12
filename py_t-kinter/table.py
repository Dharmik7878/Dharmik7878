import tkinter as tk
from tkinter import *

p=tk.Tk()
p.geometry("500x500")
p.title("table")

def bonus():
    a=int(v1.get())
    for i in range(1,11):
        print(a,"*",i,"=",i*a)
        v2.set("Your numner table is:"+str(a))
    
v1=StringVar()
v2=StringVar()

ln=tk.Label(p,text="Enter any number:").grid(row=0,column=0)
tn=tk.Entry(p,textvariable=v1).grid(row=0,column=1)

btnbonus=tk.Button(p,text="calculate table",width=10,command=bonus).grid(row=2,column=1)

lans=tk.Label(p,text="",textvariable=v2).grid(row=3,column=1)
