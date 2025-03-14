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

class fileModel:

    def __init__(self):
        """
        Initialize an empty self; reference to current instance of class fileModel
        so we can access the data provided by the uploaded CSV 

        Args:
            self: current instance of fileModel
        """
        self.data = None

    def load_csv(self, filepath):
        """
        Load provided csv file into a pandas dataframe

        Args:
            self: instance of fileModel
            filepath: csv object to be loaded into pd

        Returns: 
            True: self as dataframe

        Raises:
            FileNotFound
        """
        try: 
            self.data = pd.read_csv(filepath)
            return True
        except Exception as e:
                return f"Error loading CSV: {e}"