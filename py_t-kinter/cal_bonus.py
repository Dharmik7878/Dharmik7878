import tkinter as tk
from tkinter import *

p=tk.Tk()
p.geometry("500x500")
p.title("compny bonus")

def bonus():
    sa=int(v1.get())
    da=sa*(10/100)
    hra=sa*(15/100)
    bonus=sa*(8/100)
    gs=da+hra+bonus
    v2.set("Your gross salry is:"+str(gs))
    
v1=StringVar()
v2=StringVar()

ln=tk.Label(p,text="Enter your name:").grid(row=0,column=0)
tn=tk.Entry(p).grid(row=0,column=1)

ls=tk.Label(p,text="Enter your salary:").grid(row=1,column=0)
ts=tk.Entry(p,textvariable=v1).grid(row=1,column=1)
btnbonus=tk.Button(p,text="Gross salary",width=10,command=bonus).grid(row=2,column=1)
lans=tk.Label(p,text="",textvariable=v2).grid(row=3,column=1)
