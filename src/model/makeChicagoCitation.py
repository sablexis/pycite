"""
Creating Chicago formatted citations for thesis data

This module contains all functions related to creation of properly formatted Chicago citations from the thesis data.

Dependencies:
    - pandas

Author: Sabrina Sandy 
Date: June 10, 2025
"""

# Third-party imports
import pandas as pd

def make_Chicago_Citation(cleaned_theses_df):
    """
    taking the name, title, date and publication info 
    from previously created columns to generate new Chicago citations

    Args:
    cleaned_theses_df(df): data frame of cleaned data

    Returns:
    cleaned_csv(csv): csv data of theses with additional Chicago citation column


    """

    # use a copy of our org. data
    dfToCite = pd.read_csv('cleaned_csv.csv')
    # create a df of said data
    chiDF = pd.DataFrame(dfToCite)

    """
    The citation style for Chicago is as follows

    N: First Last, "Title" (Undergraduate Thesis, Institution, Year),pp-pp.

1. Tara Hostetler, “Bodies at War: Bacteriology and the Carrier Narratives of ‘Typhoid Mary’” (master’s thesis, Florida State University, 2007), 15-16. 

B: 

Hostetler, Tara. "Bodies at War: Bacteriology and the Carrier Narratives of ‘Typhoid Mary.’” Master’s thesis, Florida State University, 2007. 

     this will require columns:
        dc.contributor.author
        dc.date.issued
        dc.identifier.uri
        dc.publisher
        dc.title
        dc.contributor.author.last
        dc.contributor.author.first.inital
        dc.contributor.author.middle.inital
    """


    dfToCite['Chicago.citation'] = [
        (
            f"{row['dc.contributor.author']} "
            f"{row['dc.contributor.author.last']}, "
            f''' "{row['dc.title']}" '''
            f"(Undergraduate Thesis, Mount Allision University, "
            f"{row['dc.date.issued']}), pp-pp."
            f"\n"
            f"\n"
            f"{row['dc.contributor.author.last']}, "
            f"{row['dc.contributor.author']}. "
            f''' "{row['dc.title']}" '''
            f"(Undergraduate Thesis, Mount Allision University, "
            f"{row['dc.date.issued']})."

        )
        for i, row in dfToCite.iterrows()

    ]

    print(dfToCite.head())

    dfToCite.to_csv('cleaned_csv.csv')