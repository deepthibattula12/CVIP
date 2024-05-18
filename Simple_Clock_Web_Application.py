import sys
from tkinter import *
import time
def timing():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,timing)
root=Tk()
root.geometry("600x300")
root.title("Simple Clock")
clock=Label(root,font=("times",60,"bold"),bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()
digital=Label(root,font="times 24 bold")
digital.grid(row=0,column=2)
no=Label(root,text="hours        minutes        seconds",font="times 15 bold")
no.grid(row=3,column=2)
root.mainloop()