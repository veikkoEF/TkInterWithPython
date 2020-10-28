from tkinter import *

# Ein Fenster erstellen
window = Tk()
window.geometry("400x400")
# Den Fenstertitle erstellen
window.title("Hello World")

# Definition von GUI-Elementen
myName =StringVar()
myName.set("Max Mustermann")

entry = Entry(window, width="150", textvariable=myName)



# Hinzufügen der Elemente zum Fenster
entry.pack(padx=20, pady =20)

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()