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
# window specifics
window = Tk()
window.geometry('425x150')
window.title('Pycite')

# window options

def getCSV():
    return askopenfile()



# frame
top_frame = ttk.Frame(window)
btm_frame = ttk.Frame(window)

# top frame layout
top_frame.pack(side=TOP)
inst_label = ttk.Label(top_frame, text='upload a csv file and choose a citation style')
csvButton = ttk.Button(top_frame, text='upload a csv file', command=getCSV)
inst_label.pack()
csvButton.pack()


# bottom frame layout
btm_frame.pack(side=BOTTOM)

# citation btns
radio_var = tk.StringVar()
radioMLA = ttk.Radiobutton(btm_frame, text='MLA Citation', value = 0, variable= radio_var)
radioMLA.grid(column=1, row=1)



radioAPA = ttk.Radiobutton(btm_frame, text='APA Citation', value = 1, variable= radio_var)
radioAPA.grid(column=2, row=1)


radioCHI = ttk.Radiobutton(btm_frame, text='Chicago Citation', value = 2, variable= radio_var)
radioCHI.grid(column=3, row=1)


radioALL = ttk.Radiobutton(btm_frame, text='All Styles', value = 3, variable= radio_var)
radioALL.grid(column=4, row=1)


#layout


#csvFile = askopenfile()
#csvButton.pack()


window.mainloop()