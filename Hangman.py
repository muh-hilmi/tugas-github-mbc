from tkinter import *
from string import ascii_uppercase

window = Tk()
window.title("Hangman")

word_list = ["INDONESIA","MALAYSIA","THAILAND","LAOS","NORWAY","ARGENTINA","ICELAND","GERMANY","TURKEY","JAPAN"]

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def guess():
    global numberOfGuesses

imglabel = Label(window)
imglabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
imglabel.config(image=photos[0])

lblword=StringVar()
Label(window, textvariable=lblword, font=("consolas 24")).grid(row=0, column=3, columnspan=5, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c : guess(c), font=("Arial", 18), width=4).grid(row=1+n//9, column=n%9)
    n+=1

window.mainloop()