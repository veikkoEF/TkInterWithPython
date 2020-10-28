from tkinter import *
# Ein Fenster erstellen
window = Tk()
# Den Fenstertitle erstellen
window.title("Hello World")

# Menüleiste erstellen 
menuleiste = Menu(window)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf die Menüeinträge sollen weitere Einträge erscheinen.
datei_menu.add_command(label="Neu")
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Beenden", command=window.quit)

menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Hilfe", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen dem Fenster übergeben
window.config(menu=menuleiste)     

# Ereignisschleife auf Reaktion des Benutzers warten.
window.mainloop()
