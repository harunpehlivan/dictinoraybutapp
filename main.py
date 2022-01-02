from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
dictionary = PyDictionary()

root.geometry("400x400")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Adjective'][0])
    synonym.config(text = dictionary.synonym(word.get()))
    antonym.config(text = dictionary.antonym(word.get()))

Label(root, text = 'DICTIONARY IN REPLIT!', font = 'times 14 bold', fg = 'Orange').pack(pady = 10)

frame1 = Frame(root)
Label(frame1, text = 'Type word here', font = 'times 14 bold').pack(side = LEFT)
word = Entry(frame1, font = 'times 14 bold')
word.pack()
frame1.pack()

frame2 = Frame(root)
Label(frame1, text = 'Meaning: ', font = 'times 14 bold').pack(side = LEFT)
meaning = Label(frame2, text = "", font = 'times 14 bold')
meaning.pack()
frame2.pack(pady = 10)

frame3 = Frame(root)
Label(frame2, text = 'Synonym/s: ', font = 'times 14 bold').pack(side = LEFT)
synonym = Label(frame3, text = "", font = 'times 14 bold')
synonym.pack()
frame3.pack(pady = 10)

frame4 = Frame(root)
Label(frame4, text = 'Antonym/s: ', font = 'times 14 bold').pack(side = LEFT)
antonym = Label(frame4, text = "", font = 'times 14 bold')
antonym.pack()
frame4.pack(pady = 10)

Button(root, text = 'Press or click me!!', font = 'times 14 bold', command = dict).pack()

root.mainloop()
#end of code