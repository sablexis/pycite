"""
 GUI for pycite program

Communicate to the user through a graphical interface

Author: Sabrina Sandy 
Date: Sept 20, 2025
"""

from tkinter import *
from tkinter.filedialog import askopenfile

window = Tk()
csvFile = askopenfile()

window.mainloop()