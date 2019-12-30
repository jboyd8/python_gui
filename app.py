import tkinter as tk
from tkinter import filedialog, Text
import os

# This holds the whole structure
root = tk.Tk()

# Canvas sets the size of the GUI and color
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
# used to actually attach the canvas
canvas.pack()

# Almost acts like a DIV from HTML - adds more parts to the GUI
frame = tk.Frame(root, bg='white')
# rely and relx being equal centres the frame inside the GUI
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.mainloop()