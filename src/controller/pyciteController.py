"""
Controls main flow of pycite operations

Dependencies:
    - 

Usage:


Author: Sabrina Sandy
Date: March 11, 2025
"""

# Standard Library Imports
import sys
# sys.path.append('../model')

# 3rd Party Imports
import pandas as pd

# Local imports
from model.getFile import CSVFile

from view.userView import View

from model.cleaningNames import clean_theses_data

class citeController:
    def __init__(self, filepath):
        self.model = CSVFile(filepath)
        self.view = View()


    def run(self):
        """
        control the flow of pycite program
        
        Args:
            self (self): curr instance
            
        """
        # self.view.show_message("Please paste the filepath of your csv file! ")

        # file_path = self.view.get_file_input()
        #result = self.model.load_csv(self.filepath)

        theses_df = self.model.load_csv()

        if theses_df is not None:
            cleaned_df = clean_theses_data(theses_df)
            self.view.show_message("Cleaned Data")
            

        else:
            self.view.show_message("Failed to load the CSV file.")