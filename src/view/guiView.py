"""
 GUI for pycite program

Communicate to the user through a graphical interface

Author: Sabrina Sandy 
Date: Sept 20, 2025
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

from tkinter.filedialog import askopenfile

class GUIView:

    def __init__(self, root, import_func, run_func):
        self.root = root
        self.import_func = import_func
        self.run_func = run_func


        # window specifics
        self.root.geometry('425x150')
        self.root.title('Pycite')
        

        # frame
        top_frame = ttk.Frame(self.root)
        btm_frame = ttk.Frame(self.root)

        # top frame layout
        top_frame.pack(side=TOP)
        inst_label = ttk.Label(top_frame, text='upload a csv file, choose a citation style and then click generate')
        csvButton = ttk.Button(top_frame, text='upload a csv file', command= self.open_csv)
        genButton = ttk.Button(top_frame, text='generate', command= self.gen_cite)

        inst_label.pack(fill=BOTH)
        csvButton.pack()
        genButton.pack(side=BOTTOM)


        # bottom frame layout
        btm_frame.pack(side=BOTTOM)

        # citation btns
        self.radio_var = tk.StringVar()
        radioMLA = ttk.Radiobutton(btm_frame, text='MLA Citation', value = 1, variable= self.radio_var)
        radioMLA.grid(column=1, row=1)



        radioAPA = ttk.Radiobutton(btm_frame, text='APA Citation', value = 2, variable= self.radio_var)
        radioAPA.grid(column=2, row=1)


        radioCHI = ttk.Radiobutton(btm_frame, text='Chicago Citation', value = 3, variable= self.radio_var)
        radioCHI.grid(column=3, row=1)


        radioALL = ttk.Radiobutton(btm_frame, text='All Styles', value = 4, variable= self.radio_var)
        radioALL.grid(column=4, row=1)


    #funcs
    def open_csv(self):
        file = askopenfile()
        if not file:
            return
        
        csv_path = getattr(file, "name", None)
        if csv_path:
            self.import_func(csv_path)
        #print(csv_path)

    def gen_cite(self):
        cite_opt = self.radio_var.get()
        print(cite_opt)
        self.run_func(cite_opt)


    #csvFile = askopenfile()
    #csvButton.pack()


    # return window.mainloop()