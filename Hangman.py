from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window = Tk()
window.title("Hangman")

word_list = ["INDONESIA","MALAYSIA","THAILAND","LAOS","NORWAY","ARGENTINA","ICELAND","GERMANY","TURKEY","JAPAN", 
             "INDIA","MOROCCO","PAKISTAN","NEPAL","HAITI","MEXICO"]

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    imglabel.config(image=photos[0])
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblword.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11 :
        txt = list(the_word_withSpaces)
        guessed = list(lblword.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblword.set("".join(guessed))
                if lblword.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman!", "Yeay!, Kamu berhasil nebak")
                    newGame()
        else:
            numberOfGuesses+=1
            imglabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman!", "Yah kalah, silahkan coba lagi")
                newGame()

imglabel = Label(window)
imglabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
imglabel.config(image=photos[0])

lblword=StringVar()
Label(window, textvariable=lblword, font=("consolas 24")).grid(row=0, column=3, columnspan=5, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c : guess(c), font=("Arial", 18), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text = "New Game", command=lambda:newGame(), font=("Arial", 10)).grid(row=3, column=8, sticky="NSWE")


newGame()
window.mainloop()