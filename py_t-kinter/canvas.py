import tkinter as tk
from tkinter import *
top=tk.Tk()
top.geometry("555x555")
top.title("canvas")

c=tk.Canvas(top,bg="Yellow",height=300,width=300)
line=c.create_line(120,60,120,20,fill="red")
ovel=c.create_oval(210,80,90,180,fill="black")
c.pack()
