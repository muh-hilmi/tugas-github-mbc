from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window = Tk()
window.title("Hangman (Tebak Negara)")

list_negara = ["INDONESIA","MALAYSIA","THAILAND","LAOS","NORWAY","ARGENTINA","ICELAND","GERMANY","TURKEY","JAPAN", 
             "INDIA","MOROCCO","PAKISTAN","NEPAL","HAITI","MEXICO"]

gambar = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def newGame():
    global kata_kosong
    global tebak_ke
    global negara_soal
    tebak_ke = 0
    imglabel.config(image=gambar[0])
    negara_soal = random.choice(list_negara)
    kata_kosong = " ".join(negara_soal)
    lblkata.set(" ".join("_"*len(negara_soal)))

def tebak(huruf):
    global tebak_ke
    if tebak_ke < 11 :
        txt = list(kata_kosong)
        guessed = list(lblkata.get())
        if kata_kosong.count(huruf)>0:
            for c in range(len(txt)):
                if txt[c]==huruf:
                    guessed[c]=huruf
                lblkata.set("".join(guessed))
                if lblkata.get()==kata_kosong:
                    messagebox.showinfo("Hangman", "Yeay!, Kamu berhasil nebak")
                    newGame()
        else:
            tebak_ke+=1
            imglabel.config(image=gambar[tebak_ke])
            if tebak_ke == 11:
                messagebox.showwarning("Hangman", "Yah kalah, silahkan coba lagi")
                messagebox.showinfo("Hangman", 'Jawabannya : '+ negara_soal)
                newGame()

imglabel = Label(window)
imglabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
imglabel.config(image=gambar[0])

lblkata=StringVar()
Label(window, textvariable=lblkata, font=("consolas 24")).grid(row=0, column=3, columnspan=5, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c : tebak(c), font=("Arial", 18), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text = "New Game", command=lambda:newGame(), font=("Arial", 10)).grid(row=3, column=8, sticky="NSWE")

newGame()
window.mainloop()