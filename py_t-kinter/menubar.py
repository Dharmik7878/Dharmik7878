from tkinter import *

top=Tk()
top.geometry("555x555")
top.title("menubar")

def BCA():
    lans.config(text="BCA course")

def BBA():
    lans.config(text="BBA course")

def BCOM():
    lans.config(text="BCOM course")

menubtn=Menubutton(top,text="course",bd=3)

menubtn.menu=Menu(menubtn)
menubtn["menu"]=menubtn.menu

var1=IntVar()
var2=IntVar()
var3=IntVar()

menubtn.menu.add_checkbutton(label="BCA",variable=var1,command=BCA)
menubtn.menu.add_checkbutton(label="BBA",variable=var2,command=BBA)
menubtn.menu.add_checkbutton(label="BCOM",variable=var3,command=BCOM)

menubtn.pack()

lans=Label(top,text="")
lans.pack()
