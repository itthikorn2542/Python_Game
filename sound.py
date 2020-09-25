from tkinter import *
from winsound import *

root = Tk() # create tkinter window

play = lambda: PlaySound('Sound.wav', SND_FILENAME)
button = Button(root, text = 'Play', command = play)

button.pack()
root.mainloop()
