import tkinter as tk
from tkinter import *

p=tk.Tk()
p.geometry("500x500")
p.title("radio button")

def show():
    if v1.get()==1:
        lans.config(text="You are male")
    elif v1.get()==2:
        lans.config(text="You are female")
    else:
        lans.config(text="select any one option")

v1=IntVar()

lt=tk.Label(p,text="Select Your gender:")
rm=tk.Radiobutton(p,text="Male",variable=v1,value=1)
rf=tk.Radiobutton(p,text="Female",variable=v1,value=2)
bs=tk.Button(p,text="save",command=show)
lans=tk.Label(p,text="")

lt.pack()
rm.pack()
rf.pack()
bs.pack()
lans.pack()
