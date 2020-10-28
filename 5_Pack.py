from tkinter import *
from tkinter import messagebox 

# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

# Definition von GUI-Elementen
button=Button(window, text="OK")
button2=Button(window, text="Abbrechen")

# Hinzufügen der Elemente zum Fenster
button.pack(side=LEFT, padx="20", pady="20")
button2.pack(side=LEFT, padx="20", pady="20")

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()

