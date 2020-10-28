from tkinter import *
from tkinter import messagebox

# Event-Definition 
def button_action():
    messagebox.showinfo(message="Eine Meldung", title = "Infos")
    

# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

# Definition von GUI-Elementen
button = Button(window, text="OK", command=button_action)
label = Label(window, text="Ein Label")

# Hinzufügen der Elemente zum Fenster
button.pack()
label.pack()

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()

