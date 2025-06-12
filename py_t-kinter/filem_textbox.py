import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("555x555")
top.title("textbox")

def text_load():
    with open("myfile.txt","r")as file:
        data=file.read()
        tadd.insert(tk.END,data)

tadd=tk.Text(top,height=5,width=30)
tadd.pack()

text_load()
