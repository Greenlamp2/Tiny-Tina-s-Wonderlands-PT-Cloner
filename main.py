import tkinter as tk

from WonderlandsSave import WonderlandsSave
from ui import ptClonerUI, menu
from utils.utils import Constants
from tkinter import filedialog as fd


class TTWPtCloner:
    def __init__(self):
        self.ui = None
        self.debug_mode = True
        self.save_from = None
        self.save_path_from = None
        self.save_to = None
        self.save_path_to = None
        self.new_save = None

    def unlock_proceed(self):
        if self.save_from and self.save_to:
            self.ui.Button2.configure(state="normal")
            self.ui.Label1.configure(text='''Ready !''')

    def update_fields_from(self):
        if self.save_from:
            self.ui.text_save_from.set(self.save_path_from)
            self.ui.text_name_from.set(self.save_from.get_char_name())
            self.ui.text_level_from.set(self.save_from.get_level())
            first_class = self.save_from.get_first_class()
            second_class = self.save_from.get_second_class()
            first_class_name = Constants.get_class_key(first_class)
            second_class_name = Constants.get_class_key(second_class)
            self.ui.text_class_from.set(first_class_name)
            self.ui.text_second_class_from.set(second_class_name)
            self.unlock_proceed()

    def update_fields_to(self):
        if self.save_to:
            self.ui.text_save_to.set(self.save_path_to)
            self.ui.text_name_to.set(self.save_to.get_char_name())
            self.ui.text_level_to.set(self.save_to.get_level())
            first_class = self.save_to.get_first_class()
            second_class = self.save_to.get_second_class()
            first_class_name = Constants.get_class_key(first_class)
            second_class_name = Constants.get_class_key(second_class)
            self.ui.text_class_to.set(first_class_name)
            self.ui.text_second_class_to.set(second_class_name)
            self.unlock_proceed()

    def load_save_from(self, path):
        self.save_from = WonderlandsSave(path)
        self.update_fields_from()

    def load_save_to(self, path):
        self.save_to = WonderlandsSave(path)
        self.update_fields_to()

    def open_from(self):
        self.save_path_from = menu.open()
        self.load_save_from(self.save_path_from)

    def open_to(self):
        self.save_path_to = menu.open()
        self.load_save_to(self.save_path_to)

    def save_as(self):
        f = fd.asksaveasfile(mode='w', filetypes=[('Save File', '*.sav')])
        if f is None:
            return
        self.new_save.save_to(f.name)
        self.ui.Label1.configure(text='''Success !''')

    def start_gui(self):
        global root
        root = tk.Tk()
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        global _top1, _w1
        _top1 = root
        _w1 = ptClonerUI.Toplevel1(self, _top1)
        root.mainloop()

    def proceed(self):
        self.new_save = self.save_to
        self.new_save.clone_PT(self.save_from)
        self.save_as()


if __name__ == '__main__':
    editor = TTWPtCloner()
    editor.start_gui()
