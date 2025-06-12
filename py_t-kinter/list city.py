import tkinter as tk
from tkinter import *
top=tk.Tk()
top.geometry("555x555")
top.title("list box")

lcity=tk.Listbox(top,height=10,width=15)
lcity.insert(1,"Ahmedabad")
lcity.insert(2,"bhavnagr")
lcity.insert(3,"jamnagar")
lcity.insert(4,"gandhinagar")
lcity.insert(5,"gift city")
lcity.pack()
