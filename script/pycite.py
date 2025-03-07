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

# Standard library imports
import csv
import os
import argparse
from typing import List, Dict

# Third-party imports
import pandas as pd

# Constants
OUTPUT_DIR = "processed_data"
REQUIRED_COLUMNS = ["date", "value", "category"]

"""
So since we in the future we want to be able to add MLA & Chicago citations, it's important that we find the commonalities amongst all citations:
First Name, Last Name, Title, Year are all variables that are important to each citation style
Institution, Thesis & Database are common amongst the three but will be hard coded since

Names:  dc.contributor.author
Title:  dc.title
Year:   dc.date.issued


The data isn't super clean 

dc.contributor.author: need to abbreviate first and middle names to initials 
dc.title: capitalize first letter of title and subtitle, proper nouns (actually, I’ll just work on cleaning these so you can take them directly). 
dc.date.issued: need to get year only (dates are still a bit messy). 


"""


def parse_csv(filepath: str) -> pd.DataFrame:
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
    
    return data