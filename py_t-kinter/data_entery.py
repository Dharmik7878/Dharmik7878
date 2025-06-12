import tkinter as tk
top=tk.Tk()
top.geometry("500x500")
top.title("Data Entry")

def show():
    name=(tname.get())
    lans.config(text="Your name is "+name)

lname=tk.Label(top,text="Enter the name:")
lname.pack()

tname=tk.Entry(top)
tname.pack()

btnsave=tk.Button(top,text="save",command=show)
btnsave.pack()

lans=tk.Label(top,text="")
lans.pack()

