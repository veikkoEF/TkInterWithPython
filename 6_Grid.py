from tkinter import *
from tkinter import messagebox 

# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

# Definition von GUI-Elementen
button1=Button(window, text="100")
button2=Button(window, text="2")
button3=Button(window, text="3")
button4=Button(window, text="4")

# Hinzufügen der Elemente zum Fenster
button1.grid(row=0, column=0, padx=20, pady =20)
button2.grid(row=0, column=1, padx=20, pady =20)
button3.grid(row=1, column=0, padx=20, pady =20)
button4.grid(row=1, column=1, padx=20, pady =20)

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()