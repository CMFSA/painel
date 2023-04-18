import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.geometry("700x500") # the application window size
root.title("I need a NAME!") # title of window

def file_dialog():
    filename = filedialog.askopenfilename(
        initialdir="Downloads",
        title="Select A File To Start",
        filetypes=(
            ("mp4 files", "*.mp4"),
            ("mov files", "*.mov"),
            ("png files", "*.png"),
            ("jpeg files", "*.jpeg"),
            ("jpg files", "*.jpg")))

    if filename:
        root.img = tk.PhotoImage(file=filename)
        root.iconphoto( False, root.img ) # application icon

app = tk.Toplevel(root)
app.transient( root )
button = tk.Button(app, text="Start!", command=file_dialog)
button.pack(fill = "both", expand = True)

root.mainloop()

print("Successful Build")