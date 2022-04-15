#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 15, 2022 07:08:59 PM CEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

class Toplevel1:
    def __init__(self, ptClonerUI_support, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.parent = ptClonerUI_support
        self.parent.ui = self

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x581+560+240")
        top.minsize(120, 1)
        top.maxsize(7444, 1061)
        top.resizable(0,  0)
        top.title("TTW PTcloner")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.text_save_from = tk.StringVar()
        self.text_name_from = tk.StringVar()
        self.text_level_from = tk.StringVar()
        self.text_class_from = tk.StringVar()
        self.text_second_class_from = tk.StringVar()
        self.text_save_to = tk.StringVar()
        self.text_name_to = tk.StringVar()
        self.text_level_to = tk.StringVar()
        self.text_class_to = tk.StringVar()
        self.text_second_class_to = tk.StringVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(x=0, y=0, height=580, width=800)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(x=10, y=10, height=400, width=380)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''From''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(x=15, y=20, height=60, width=350, bordermode='ignore')

        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=ptClonerUI_support.open_from)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''')

        self.Labelframe2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2.place(x=15, y=90, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Save file path''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Labelframe2)
        self.Entry1.place(x=10, y=20, height=20, width=324, bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(state='readonly')
        self.Entry1.configure(textvariable=self.text_save_from)

        self.Labelframe2_2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_2.place(x=15, y=150, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2.configure(relief='groove')
        self.Labelframe2_2.configure(foreground="black")
        self.Labelframe2_2.configure(text='''Name''')
        self.Labelframe2_2.configure(background="#d9d9d9")
        self.Labelframe2_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2.configure(highlightcolor="black")

        self.Entry1_2 = tk.Entry(self.Labelframe2_2)
        self.Entry1_2.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")
        self.Entry1_2.configure(state='readonly')
        self.Entry1_2.configure(textvariable=self.text_name_from)

        self.Labelframe2_2_2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_2_2.place(x=15, y=210, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2.configure(relief='groove')
        self.Labelframe2_2_2.configure(foreground="black")
        self.Labelframe2_2_2.configure(text='''Level''')
        self.Labelframe2_2_2.configure(background="#d9d9d9")
        self.Labelframe2_2_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2.configure(highlightcolor="black")

        self.Entry1_2_2 = tk.Entry(self.Labelframe2_2_2)
        self.Entry1_2_2.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2.configure(background="white")
        self.Entry1_2_2.configure(cursor="fleur")
        self.Entry1_2_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2.configure(font="TkFixedFont")
        self.Entry1_2_2.configure(foreground="#000000")
        self.Entry1_2_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2.configure(highlightcolor="black")
        self.Entry1_2_2.configure(insertbackground="black")
        self.Entry1_2_2.configure(selectbackground="blue")
        self.Entry1_2_2.configure(selectforeground="white")
        self.Entry1_2_2.configure(state='readonly')
        self.Entry1_2_2.configure(textvariable=self.text_level_from)

        self.Labelframe2_2_2_1 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_2_2_1.place(x=15, y=270, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2_1.configure(relief='groove')
        self.Labelframe2_2_2_1.configure(foreground="black")
        self.Labelframe2_2_2_1.configure(text='''First class''')
        self.Labelframe2_2_2_1.configure(background="#d9d9d9")
        self.Labelframe2_2_2_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2_1.configure(highlightcolor="black")

        self.Entry1_2_2_1 = tk.Entry(self.Labelframe2_2_2_1)
        self.Entry1_2_2_1.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2_1.configure(background="white")
        self.Entry1_2_2_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2_1.configure(font="TkFixedFont")
        self.Entry1_2_2_1.configure(foreground="#000000")
        self.Entry1_2_2_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2_1.configure(highlightcolor="black")
        self.Entry1_2_2_1.configure(insertbackground="black")
        self.Entry1_2_2_1.configure(selectbackground="blue")
        self.Entry1_2_2_1.configure(selectforeground="white")
        self.Entry1_2_2_1.configure(state='readonly')
        self.Entry1_2_2_1.configure(textvariable=self.text_class_from)

        self.Labelframe2_2_2_1_1 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2_2_2_1_1.place(x=15, y=330, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2_1_1.configure(relief='groove')
        self.Labelframe2_2_2_1_1.configure(foreground="black")
        self.Labelframe2_2_2_1_1.configure(text='''Second class''')
        self.Labelframe2_2_2_1_1.configure(background="#d9d9d9")
        self.Labelframe2_2_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2_1_1.configure(highlightcolor="black")

        self.Entry1_2_2_1_1 = tk.Entry(self.Labelframe2_2_2_1_1)
        self.Entry1_2_2_1_1.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2_1_1.configure(background="white")
        self.Entry1_2_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2_1_1.configure(font="TkFixedFont")
        self.Entry1_2_2_1_1.configure(foreground="#000000")
        self.Entry1_2_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2_1_1.configure(highlightcolor="black")
        self.Entry1_2_2_1_1.configure(insertbackground="black")
        self.Entry1_2_2_1_1.configure(selectbackground="blue")
        self.Entry1_2_2_1_1.configure(selectforeground="white")
        self.Entry1_2_2_1_1.configure(state='readonly')
        self.Entry1_2_2_1_1.configure(textvariable=self.text_second_class_from)

        self.Labelframe1_1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1_1.place(x=410, y=10, height=400, width=380)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(foreground="black")
        self.Labelframe1_1.configure(text='''To''')
        self.Labelframe1_1.configure(background="#d9d9d9")
        self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1.configure(highlightcolor="black")

        self.Button1_1 = tk.Button(self.Labelframe1_1)
        self.Button1_1.place(x=15, y=20, height=60, width=350
                , bordermode='ignore')
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(command=ptClonerUI_support.open_to)
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Browse''')

        self.Labelframe2_1 = tk.LabelFrame(self.Labelframe1_1)
        self.Labelframe2_1.place(x=15, y=90, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_1.configure(relief='groove')
        self.Labelframe2_1.configure(foreground="black")
        self.Labelframe2_1.configure(text='''Save file path''')
        self.Labelframe2_1.configure(background="#d9d9d9")
        self.Labelframe2_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_1.configure(highlightcolor="black")

        self.Entry1_1 = tk.Entry(self.Labelframe2_1)
        self.Entry1_1.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_1.configure(state='readonly')
        self.Entry1_1.configure(textvariable=self.text_save_to)

        self.Labelframe2_2_1 = tk.LabelFrame(self.Labelframe1_1)
        self.Labelframe2_2_1.place(x=15, y=150, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_1.configure(relief='groove')
        self.Labelframe2_2_1.configure(foreground="black")
        self.Labelframe2_2_1.configure(text='''Name''')
        self.Labelframe2_2_1.configure(background="#d9d9d9")
        self.Labelframe2_2_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_1.configure(highlightcolor="black")

        self.Entry1_2_1 = tk.Entry(self.Labelframe2_2_1)
        self.Entry1_2_1.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_1.configure(background="white")
        self.Entry1_2_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_1.configure(font="TkFixedFont")
        self.Entry1_2_1.configure(foreground="#000000")
        self.Entry1_2_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_1.configure(highlightcolor="black")
        self.Entry1_2_1.configure(insertbackground="black")
        self.Entry1_2_1.configure(selectbackground="blue")
        self.Entry1_2_1.configure(selectforeground="white")
        self.Entry1_2_1.configure(state='readonly')
        self.Entry1_2_1.configure(textvariable=self.text_name_to)

        self.Labelframe2_2_2_2 = tk.LabelFrame(self.Labelframe1_1)
        self.Labelframe2_2_2_2.place(x=15, y=210, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2_2.configure(relief='groove')
        self.Labelframe2_2_2_2.configure(foreground="black")
        self.Labelframe2_2_2_2.configure(text='''Level''')
        self.Labelframe2_2_2_2.configure(background="#d9d9d9")
        self.Labelframe2_2_2_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2_2.configure(highlightcolor="black")

        self.Entry1_2_2_2 = tk.Entry(self.Labelframe2_2_2_2)
        self.Entry1_2_2_2.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2_2.configure(background="white")
        self.Entry1_2_2_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2_2.configure(font="TkFixedFont")
        self.Entry1_2_2_2.configure(foreground="#000000")
        self.Entry1_2_2_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2_2.configure(highlightcolor="black")
        self.Entry1_2_2_2.configure(insertbackground="black")
        self.Entry1_2_2_2.configure(selectbackground="blue")
        self.Entry1_2_2_2.configure(selectforeground="white")
        self.Entry1_2_2_2.configure(state='readonly')
        self.Entry1_2_2_2.configure(textvariable=self.text_level_to)

        self.Labelframe2_2_2_1_2 = tk.LabelFrame(self.Labelframe1_1)
        self.Labelframe2_2_2_1_2.place(x=15, y=270, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2_1_2.configure(relief='groove')
        self.Labelframe2_2_2_1_2.configure(foreground="black")
        self.Labelframe2_2_2_1_2.configure(text='''First class''')
        self.Labelframe2_2_2_1_2.configure(background="#d9d9d9")
        self.Labelframe2_2_2_1_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2_1_2.configure(highlightcolor="black")

        self.Entry1_2_2_1_2 = tk.Entry(self.Labelframe2_2_2_1_2)
        self.Entry1_2_2_1_2.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2_1_2.configure(background="white")
        self.Entry1_2_2_1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2_1_2.configure(font="TkFixedFont")
        self.Entry1_2_2_1_2.configure(foreground="#000000")
        self.Entry1_2_2_1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2_1_2.configure(highlightcolor="black")
        self.Entry1_2_2_1_2.configure(insertbackground="black")
        self.Entry1_2_2_1_2.configure(selectbackground="blue")
        self.Entry1_2_2_1_2.configure(selectforeground="white")
        self.Entry1_2_2_1_2.configure(state='readonly')
        self.Entry1_2_2_1_2.configure(textvariable=self.text_class_to)

        self.Labelframe2_2_2_1_1_1 = tk.LabelFrame(self.Labelframe1_1)
        self.Labelframe2_2_2_1_1_1.place(x=15, y=330, height=55, width=350
                , bordermode='ignore')
        self.Labelframe2_2_2_1_1_1.configure(relief='groove')
        self.Labelframe2_2_2_1_1_1.configure(foreground="black")
        self.Labelframe2_2_2_1_1_1.configure(text='''Second class''')
        self.Labelframe2_2_2_1_1_1.configure(background="#d9d9d9")
        self.Labelframe2_2_2_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe2_2_2_1_1_1.configure(highlightcolor="black")

        self.Entry1_2_2_1_1_1 = tk.Entry(self.Labelframe2_2_2_1_1_1)
        self.Entry1_2_2_1_1_1.place(x=10, y=20, height=20, width=324
                , bordermode='ignore')
        self.Entry1_2_2_1_1_1.configure(background="white")
        self.Entry1_2_2_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_2_2_1_1_1.configure(font="TkFixedFont")
        self.Entry1_2_2_1_1_1.configure(foreground="#000000")
        self.Entry1_2_2_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_2_2_1_1_1.configure(highlightcolor="black")
        self.Entry1_2_2_1_1_1.configure(insertbackground="black")
        self.Entry1_2_2_1_1_1.configure(selectbackground="blue")
        self.Entry1_2_2_1_1_1.configure(selectforeground="white")
        self.Entry1_2_2_1_1_1.configure(state='readonly')
        self.Entry1_2_2_1_1_1.configure(textvariable=self.text_second_class_to)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(x=10, y=420, height=155, width=785)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(x=10, y=10, height=94, width=767)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=ptClonerUI_support.proceed)
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(state='disabled')
        self.Button2.configure(text='''Proceed''')

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(x=350, y=120, height=21, width=199)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Waiting ...''')