from tkinter import filedialog as fd

def open(*args):
    filename = fd.askopenfilename(filetypes=[('Save File', '*.sav')])
    return filename