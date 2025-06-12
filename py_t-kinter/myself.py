import tkinter as tk
v=tk.Tk()
v.geometry("800x900")
v.title("Your self")
lblt=tk.Label(v,text="My Self",
              #width="22",
                  foreground="red",
                  background="orange",
                  font=("monotype corsive",20,"bold")).place(x=10,y=10)
#lblt.pack()

lblt1=tk.Label(v,text="NAME: Dharmik Zanzmer",
               width="22",
                  foreground="orange",
                  background="blue",
                  font=("monotype corsive",20,"bold")).place(x=10,y=50)
#lblt1.pack()

lblt2=tk.Label(v,text="AGE: 20",
               width="22",
                  foreground="blue",
                  background="yellow",
                  font=("monotype corsive",20,"bold")).place(x=10,y=90)
#lblt2.pack()

lblt3=tk.Label(v,text="ADDRESS: Rabarika",
               width="22",
                  foreground="red",
                  background="purple",
                  font=("monotype corsive",20,"bold")).place(x=10,y=130)
#lblt3.pack()

lblt4=tk.Label(v,text="CITY: Bhavnagar",
               width="22",
                  foreground="red",
                  background="orange",
                  font=("monotype corsive",20,"bold")).place(x=10,y=170)
#lblt4.pack()

lblt5=tk.Label(v,text="MOBILE no-: 9106488799",
               width="22",
                  foreground="orange",
                  background="red",
                  font=("monotype corsive",20,"bold")).place(x=10,y=210)
#lblt5.pack()
