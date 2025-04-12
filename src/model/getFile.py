"""
reading user inputted csv files

Dependencies:
    - pandas

Usage:
    python pycite.py input.csv [options]

Author: Sabrina Sanfy 
Date: March 3, 2025
"""

# 3rd Party Imports
import pandas as pd

class CSVFile:

    def __init__(self, filepath):
        """
        Initialize an instance of this fileModel class to access instance vars & methods of fileModel
        so we can access the data provided by the uploaded CSV 

        Args:
            self: current instance of fileModel
            filepath: location of csv object to be loaded into pd

        """
        self.filepath = filepath

    def load_csv(self):
        """
        Load provided csv file into a pandas dataframe

        Args:
            self: instance of fileModel

        Returns: 
            dataframe:  unclean theses as pandas dataframe

        Raises:
            FileNotFound
        """
        try: 
            thesesCSV = pd.read_csv(self.filepath)
            return thesesCSV
        except Exception as e:
                return f"Error loading CSV: {e}"
        
    