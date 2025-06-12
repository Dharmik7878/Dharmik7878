import tkinter as tk
from tkinter import *
top=tk.Tk()
top.geometry("555x555")
top.title("canvas")

f_frame=tk.Frame(top)
f_frame.pack()
f_btn=tk.Button(f_frame,text="1",height=3,width=7)
f_btn.pack(side=LEFT)
sbtn=tk.Button(f_frame,text="2",height=3,width=7)
sbtn.pack(side=LEFT)

f_frame=tk.Frame(top)
f_frame.pack(side=BOTTOM)
f_btn=tk.Button(f_frame,text="3",height=3,width=7)
f_btn.pack(side=LEFT)
sbtn=tk.Button(f_frame,text="4",height=3,width=7)
sbtn.pack(side=LEFT)

f_frame=tk.Frame(top)
f_frame.pack(side=LEFT)
f_btn=tk.Button(f_frame,text="5",height=3,width=7)
f_btn.pack(side=LEFT)
sbtn=tk.Button(f_frame,text="6",height=3,width=7)
sbtn.pack(side=LEFT)

f_frame=tk.Frame(top)
f_frame.pack(side=RIGHT)
f_btn=tk.Button(f_frame,text="7",height=3,width=7)
f_btn.pack(side=LEFT)
sbtn=tk.Button(f_frame,text="8",height=3,width=7)
sbtn.pack(side=LEFT)
