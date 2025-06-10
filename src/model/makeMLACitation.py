"""
Creating MLA formatted citations for thesis data

This module contains all functions related to creation of properly formatted MLA citations from the thesis data.

Dependencies:
    - pandas
    - numpy

Author: Sabrina Sandy 
Date: June 6, 2025
"""

# Third-party imports
import re
import pandas as pd
import numpy as np

def make_MLA_citation(cleaned_theses_df):
     # use the copy of our data
    toCite = pd.read_csv('cleaned_csv.csv')
    toCite_df = pd.DataFrame(toCite)

    # adding extra columns for MLA
    toCite_df['MLA.citation'] = [
        (
            f"{row['dc.contributor.author.last']}, "
            f"{row['dc.contributor.author.first']}. "
            f"{row['dc.title']}. "
            f"{row['dc.date.issued']}. "
            f"{row['dc.publisher']}, Thesis. Scholaris, "
            f"{row['dc.identifier.uri']}."

        )
        for i, row in toCite_df.iterrows()
    
    ]
    
    """
    The citation style for MLA is as follows

    Last, First. Title. YYYY. Institution, Thesis. ProQuest, search.proquest.com/docview/305212264?accountid=7432. 
    """


    print(toCite_df.head())



    toCite_df.to_csv('cleaned_csv.csv')

        
