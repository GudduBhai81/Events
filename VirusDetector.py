from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Virus Detector!")
root.geometry("500x500")




def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)


root.mainloop()