import tkinter as tk
from tkinter import *
from tkinter import ttk

top=tk.Tk()
top.geometry("500x500")
top.title("combobox")

def show():
    data=v.get()
    lans.config(text=data)

v=StringVar()
lcom=tk.Label(top,text="Select Your city:",font=("Time new roman",18)).grid(row=5,column=1)

city=ttk.Combobox(top,width=20,textvariable=v)
city['value']=("ahmedabad","bhavnagar","jamnagar","gandhinagar","baroda","surat","vapi","vansda")
city.grid(row=5,column=2)

bsave=tk.Button(top,text="Submit",command=show).grid(row=6,column=1)
lans=tk.Label(top,text="").grid(row=7,column=1)
