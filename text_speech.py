from os import system
import threading
from DictionaryServices import *
import Tkinter
from Tkinter import *
from ScrolledText import *

def word_meaning(word):
	print word
	wordrange = (0, len(word))
	dictresult = DCSCopyTextDefinition(None, word, wordrange)
	if not dictresult:
		return 'Not found'
	else:
		return dictresult.encode('utf-8')

def speak(sentance):
	var.set(word_meaning(sentance))
	system("say '" + sentance + "'")



root = Tkinter.Tk()
frame = Frame(root)
frame.pack()


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Text(frame)
redbutton.pack( side = LEFT)

search = Tkinter.Button(frame, text ="Search", command = lambda: speak(redbutton.get(1.0, END)))
search.pack( side = LEFT )

var = StringVar()
textPad = Label(root,  textvariable = var, wraplength=250, width=100, height=40, relief=RAISED)
textPad.pack(side = BOTTOM)

root.mainloop()
