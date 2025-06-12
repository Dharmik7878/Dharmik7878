import tkinter as tk
from tkinter import *
from tkinter.ttk import *
top=Tk()

def show():
    import time
    progress['value']=20
    top.update_idletasks()
    time.sleep(1.0)

    progress['value']=40
    top.update_idletasks()
    time.sleep(1.0)

    progress['value']=60
    top.update_idletasks()
    time.sleep(1.0)

    progress['value']=80
    top.update_idletasks()
    time.sleep(1.0)

    progress['value']=100
    top.update_idletasks()
    time.sleep(1.0)

    if progress['value']==100:
        lblans.config(text="Thank you")
        progress['value']=0
    
progress=Progressbar(top,orient=HORIZONTAL,length=100,mode='determinate')
progress.pack(pady=10)
Button(top,text="Start", command=show).pack(pady=10)
lblans=tk.Label(top,text="")
lblans.pack()
