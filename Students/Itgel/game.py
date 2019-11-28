from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random 

window = Tk()
window.title("Hangman")
word_list = ["RUSSIA", "ARGENTINA", "MEXICO", "COLOMBIA", "KAZAKHSTAN", "GERMANY", "TURKEY", "HUNGARY", "FINLAND", "INDIA", "CHINA", "SWEDEN", "MONGOLIA", "MOROCCO", "NORWAY", "CHILE", "IRELAND", "ICELAND", "CROATIA", "ESTONIA", "SPAIN", "NIGERIA", "JAPAN", "UKRAINE", "ALGERIA"]

photos= [PhotoImage(file="C:/Users/g12/Downloads/hangman01.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman02.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman03.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman04.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman05.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman06.png"), PhotoImage(file="C:/Users/g12/Downloads/hangman07.png")]


def newGame ():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<6:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guess))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses]) 
            if numberOfGuesses==6:
                messagebox.showwarning("Hangman", "Game Over!")
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar ()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

newGame()
window.mainloop()