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
import tkinter as tk
from tkinter import *


# 3rd Party Imports
import pandas as pd

# Local imports
from model.getFile import CSVFile

from view.userView import View

from view.guiView import GUIView

from model.cleaningNames import clean_theses_data


# citation style functions
from model.makeMLACitation import make_MLA_citation
from model.makeAPACitation import make_APA_citation
from model.makeChicagoCitation import make_Chicago_Citation


class citeController:

    """
    initalize controller, import model and view 

    Args:
        self (self): curr instance of 
        root (root): parent instance for tkinter
        filepath (None): filepath obj or string of csv file to be cited
    """

    def __init__(self, root, filepath=None):
        self.root = root
        self.model = CSVFile(filepath) if filepath else None
        self.view = View()
        self.gui = GUIView(self.root, import_func=self.import_file, run_func=self.run)


    """
    import the csv file provided by the user, may be file obj or string if using terminal
    if the csv_path has the attribute name from tkinter file dialog then set string to that name
    then run the model with that csv and print the path (depriciated debug test)

    Args:
        self (self): curr instance of 
        csv_path (str): the filepath of the passed file 

    """

    def import_file(self, csv_path: str):
         if hasattr(csv_path, "name"):
              csv_path = csv_path.name
         self.model = CSVFile(csv_path)
         print(csv_path)


    """
    originally the main function that got the program running
    now is just repsonsible for the users citation choice

    Args:
        self
        usrCitationChoice (str): digit associated with citation type
    """

    def run(self, usrCitationChoice):
        """
        control the flow of pycite program
        
        Args:
            self (self): curr instance
            
        """

        # load the csv object from model func
        theses_df = self.model.load_csv()


        
        # if the data frame is not none, clean the data & create cleanded df
        if theses_df is not None:
            cleaned_df = clean_theses_data(theses_df)
            self.view.show_message("Cleaned Data")

            # create all the citation functions
            mla = make_MLA_citation(cleaned_df)
            apa = make_APA_citation(cleaned_df)
            chi = make_Chicago_Citation(cleaned_df)

            # based off user choice decide what style function to run
            if usrCitationChoice == "1":
                
                self.view.show_message("Made MLA citations")
            elif usrCitationChoice == "2":
                    apa
                    self.view.show_message("Made APA citations")
            elif usrCitationChoice == "3":
                    chi
                    self.view.show_message("Made Chicago citations")
            elif usrCitationChoice == "4":
                    mla    
                    self.view.show_message("Made MLA citations")
                    apa
                    self.view.show_message("Made APA citations")
                    chi
                    self.view.show_message("Made Chicago citations")
                    
            
        else:
            self.view.show_message("Failed to load the CSV file, cannot create citaitons.")
            
    