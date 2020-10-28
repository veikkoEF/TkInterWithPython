import tkinter as tk

def create_window():
    window2 = tk.Toplevel(root)
    label = tk.Label(window2, text="Ein Label")
    label.pack()

root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()