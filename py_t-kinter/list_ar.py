import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("500x500")
top.title("add remove")

def show():
    data=v.get()
    lcity.insert(END,data)
    v.set("")

v=StringVar()
lblcity=tk.Label(top,text="List Of City")
lcity=tk.Listbox(top,height=8,width=15)

ladd=tk.Label(top,text="Enter the new city:")
tadd=tk.Entry(top,textvariable=v)
badd=tk.Button(top,text="ADD",command=show)
bdel=tk.Button(top,text="DELETE",command=lambda
               listbox=lcity:lcity.delete(ANCHOR))
lblcity.pack()
lcity.pack()
ladd.pack()
tadd.pack()
badd.pack()
bdel.pack()
