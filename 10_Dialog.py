from tkinter import *
import tkinter.messagebox

# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

# Messagebox
result = tkinter.messagebox.askokcancel("Test", "Möchten Sie die Berechnung starten?")

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()