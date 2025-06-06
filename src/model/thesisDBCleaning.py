"""
This is cleaning the given CSV file 

Dependencies:
    - pandas
    - numpy

Usage:
    python pycite.py input.csv [options]

Author: Sabrina Sanfy 
Date: March 18, 2025
"""

# local imports
from getFile import CSVFile
from view.userView import View

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


Unfortunately the data isn't super clean 

dc.contributor.author: need to abbreviate first and middle names to initials 
dc.title: capitalize first letter of title and subtitle, proper nouns (actually, I’ll just work on cleaning these so you can take them directly). 
dc.date.issued: need to get year only (dates are still a bit messy). 


"""



def cleanThesesData(filepath):
    # Create a CSVFile instance with the provided filepath
    thesesCSV = CSVFile(filepath)

    # load the CSV file into pandas df
    thesesCSV_df = thesesCSV.load_csv()

    if thesesCSV_df is None:
        print("Error: Failed to load the CSV file.")
        return None
    
    # Print the original data for debugging
    print("Original data:")
    print(thesesCSV_df.head())
    
    # TODO: Implement data cleaning logic here
    # For example:
    # - Extract year from dc.date.issued
    # - Format author names
    # - Clean up titles

   


    return thesesCSV_df
