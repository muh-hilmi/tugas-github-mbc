from tkinter import *
from string import ascii_uppercase


window = Tk()
window.title("Hangman")

n=0
for c in ascii_uppercase:
    Button(window, text=c, font=("Arial", 18), width=4).grid(row=1+n//9, column=n%9)
    n+=1

window.mainloop()