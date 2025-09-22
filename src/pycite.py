"""
pycite theses citation maker 

This script is designed to read through a dataset of Undergraduate student theses & automatically create citatations.

Dependencies:
    - pandas
    - numpy

Usage:
    python pycite.py input.csv [options]

Author: Sabrina Sanfy 
Date: March 3, 2025
"""

# Local imports
from controller.pyciteController import citeController
from view.userView import View
from view.guiView import GUIView


# Standard library imports
import csv
import os
import argparse
import sys
import tkinter as tk
from typing import List, Dict
 

# Third-party imports
import pandas as pd



# def parse_csv(filepath: str) -> pd.DataFrame:
"""
    Parse the CSV file into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Parsed data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If required columns are missing
    """
    # Implementation here
    
    # Validate required columns are present
    # This is important because...
    
    # return data


class Main:
    @staticmethod
    def main(filepath):
        controller = citeController(filepath)
        controller.run(usrCitationChoice)
        root = tk.Tk()
        root.title("Pycite Main")
        root.mainloop

if __name__ == "__main__":
    
    filepath = View.get_file_input()
    View.citationOptions()
    view = View()
    usrCitationChoice = view.chooseCitation

    controller = citeController(filepath)
    controller.run(usrCitationChoice)
    

    Main.main(filepath)