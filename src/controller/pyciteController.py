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

# citation style functions
from model.makeMLACitation import make_MLA_citation
from model.makeAPACitation import make_APA_citation
from model.makeChicagoCitation import make_Chicago_Citation


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
        usrCitationChoice = ""
        usrCitationChoice = self.view.chooseCitation

        if theses_df is not None:
            cleaned_df = clean_theses_data(theses_df)
            self.view.show_message("Cleaned Data")

            if usrCitationChoice == "1":
                
                mla = make_MLA_citation(theses_df)
                self.view.show_message("Made MLA citations")
            elif usrCitationChoice == "2":
                    apa = make_APA_citation(cleaned_df)
                    self.view.show_message("Made APA citations")
            elif usrCitationChoice == "3":
                    chi = make_Chicago_Citation(cleaned_df)
                    self.view.show_message("Made Chicago citations")
            elif usrCitationChoice == "4":
                    mla = make_MLA_citation(cleaned_df)
                    self.view.show_message("Made MLA citations")
                    apa = make_APA_citation(cleaned_df)
                    self.view.show_message("Made APA citations")
                    chi = make_Chicago_Citation(cleaned_df)
                    self.view.show_message("Made Chicago citations")
        else:
            self.view.show_message("Failed to load the CSV file.")
            
    