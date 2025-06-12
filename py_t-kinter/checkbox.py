import tkinter as tk
from tkinter import *

p=tk.Tk()
p.geometry("500x500")
p.title("Checkbox")

def show():
    if v1.get()==1 and v2.get()==1 and v3.get()==1:
        lblans.config(text="Your hobbies is playing, reading and dancing")
    elif v1.get()==1 and v2.get()==1:
        lblans.config(text="Your hobbies is playing and reading")
    elif v2.get()==1 and v3.get()==1:
        lblans.config(text="Your hobbies is reading and dancing")
    elif v1.get()==1 and v3.get()==1:
        lblans.config(text="Your hobbies is playing and dancing")
    elif v1.get()==1:
        lblans.config(text="Your hobbies is playing")
    elif v2.get()==1:
        lblans.config(text="Your hobbies is reading")
    elif v3.get()==1:
        lblans.config(text="Your hobbies is dancing")
    else:
        lblans.config(text="plz select Your hobbies")

v1=IntVar()
v2=IntVar()
v3=IntVar()

lt=tk.Label(p,text="Select Your Hobbies!")
c1=tk.Checkbutton(p,text="playing",variable=v1,onvalue=1,offvalue=0)
c2=tk.Checkbutton(p,text="Reading",variable=v2,onvalue=1,offvalue=0)
c3=tk.Checkbutton(p,text="Dancing",variable=v3,onvalue=1,offvalue=0)
btnsave=tk.Button(p,text="Save",command=show)
lblans=tk.Label(p,text="")

lt.pack()
c1.pack()
c2.pack()
c3.pack()
btnsave.pack()
lblans.pack()
