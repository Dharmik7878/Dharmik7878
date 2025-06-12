import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("555x555")
top.title("texttbox")

tadd=tk.Text(top,height=8,width=35,bd=5)
tadd.insert(INSERT,"dhamo ")
tadd.insert(END,"computer")

tadd.tag_add("tag1","1.0","1.5")
tadd.tag_add("tag2","1.6","1.14")

tadd.tag_config("tag1",background="Yellow",foreground="Red",)
tadd.tag_config("tag2",background="Blue",foreground="Yellow",
                font=("Monotype conrsiva",22,"bold"))

tadd.pack()
