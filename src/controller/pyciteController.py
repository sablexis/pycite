"""
Controls main flow of pycite operations

Dependencies:
    - 

Usage:


Author: Sabrina Sandy
Date: March 11, 2025
"""

# Local imports

from model.getFile import fileModel
from view.userView import View

class citeController:
    def __init__(self):
        self.model = fileModel()
        self.view = View()


    def run(self):
        """
        control the flow of pycite program
        
        Args:
            self (self): curr instance
            
        """
        self.view.show_message("Please paste the filepath of your csv file! ")

        file_path = self.view.get_file_input()
        result = self.model.load_csv(file_path)

        