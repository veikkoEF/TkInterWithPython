from tkinter import *
from tkinter import messagebox

def hello(event):
    print("Hallo") 
def quit(event):                           
    print("Doppelklick zum Beenden") 
    import sys; sys.exit() 
    

# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()





