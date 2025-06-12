from tkinter import *
from tkinter import *
import os
from tkinter.messagebox import *
from tkinter import filedialog,simpledialog
top=Tk()
top.geometry("555x555")
top.title("menubar2")

def cut():
    txtadd.event_generate("<<Cut>>")

def copy():
    txtadd.event_generate("<<Copy>>")

def paste():
    txtadd.event_generate("<<Paste>>")

def select():
    txtadd.event_generate("<<SelectAll>>")

def new():
    txtadd.delete(1.0,END)

def save():
    fd=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if fd!=None:
        data=txtadd.get(1.0,END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="error",message="not able to save this file")

def open1():
    fd=filedialog.askopenfile(parent=top,mode="r")
    t=fd.read()
    txtadd.delete(0.0,END)
    txtadd.insert(0.0,t)

def saveas():
    fd=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    t=txtadd.get(0.0,END)
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error",message="Not able to save as file")

def delete():
    txtadd.event_generate("<<Clear>>")

def td():
    now=datetime.now()
    dtString=now.strftime("%h:%m:%s %d/%m/%y")
    txtadd.config(text=""+str(dtString))

menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New",command=new)
file.add_command(label="Open",command=open1)
file.add_command(label="Save",command=save)
file.add_command(label="Save As...",command=saveas)
file.add_separator()
file.add_command(label="Exit",command=top.destroy)
menubar.add_cascade(label="file",menu=file)

edit=Menu(menubar,tearoff=0)
edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="cut",command=cut)
edit.add_command(label="copy",command=copy)
edit.add_command(label="past",command=paste)
edit.add_command(label="delete",command=delete)
edit.add_separator()
edit.add_command(label="select all",command=select)
edit.add_command(label="time/date",command=td)
edit.add_separator()
edit.add_command(label="font")
menubar.add_cascade(label="edit",menu=edit)

view=Menu(menubar,tearoff=0)
view.add_command(label="zoom")
view.add_command(label="status bar")
view.add_command(label="word wrap")
menubar.add_cascade(label="view",menu=view)
top.title("textbox")

top.config(menu=menubar)

txtadd=Text(top,height=20,width=70,bd=5)
txtadd.pack()
