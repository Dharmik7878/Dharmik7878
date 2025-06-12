import tkinter as tk
from tkinter import messagebox

top=tk.Tk()
top.geometry("500x500")

messagebox.showinfo("Message","Informed")

messagebox.showwarning("Message","Alert Warning")

messagebox.showerror("Message","Error")

messagebox.askquestion("Message","are you sure?")

messagebox.askokcancel("Message","Redirecting you to www.google.com")

messagebox.askyesno("Message","Got it?")

messagebox.askretrycancel("Message","Try again?")
