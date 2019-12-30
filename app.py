import tkinter as tk
from tkinter import filedialog, Text
import os

# This holds the whole structure
root = tk.Tk()
apps = []


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(("executables" ,"*.app"), ('all files', "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def runApps():
    for app in apps:
        os.open(app, os.O_RDWR)


# Canvas sets the size of the GUI and color
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
# used to actually attach the canvas
canvas.pack()

# Almost acts like a DIV from HTML - adds more parts to the GUI
frame = tk.Frame(root, bg='white')
# rely and relx being equal centres the frame inside the GUI
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Adds a button to the root element
openFile = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='black', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=10, pady=5, fg='white', bg='black', command=runApps)
runApps.pack()

root.mainloop()