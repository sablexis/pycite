"""
Creating APA formatted citations for thesis data

This module contains all functions related to creation of properly formatted APA citations from the thesis data.

Dependencies:
    - pandas
    - numpy

Author: Sabrina Sandy 
Date: June 10, 2025
"""

# Third-party imports
import pandas as pd
import numpy as np

def make_APA_citation(cleaned_theses_df):
    """
    taking the name, title, date and publication info 
    from previously created columns to generate new APA citations

    Args:
    cleaned_theses_df(df): data frame of cleaned data

    Returns:
    cleaned_csv(csv): csv data of theses with additional APA citation column


    """

    # use a copy of our org. data
    dfToCite = pd.read_csv('cleaned_csv.csv')
    # create a df of said data
    apaDF = pd.DataFrame(dfToCite)

    """
    The citation style for APA is as follows

    Lastname, F. M. (Year). Title of dissertation/thesis (Publication No.) [Doctoral dissertation/Master’s thesis, Name of Institution Awarding the Degree]. Database or Archive Name.

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


    dfToCite['APA.citation'] = [

        (
            f"{row['dc.contributor.author.last']}, "
            f"{row['dc.contributor.author.first.inital']}. "
            # check if there is a value in the middle inital col
            f"{row['dc.contributor.author.middle.inital'] + '. ' if not pd.isna(row['dc.contributor.author.middle.inital']) else ''}"
            f"("
            f"{row['dc.date.issued']}). "
            f"{row['dc.title']}) [Undergraduate Thesis, Mount Allison University]. Scholaris, "
            f"{row['dc.identifier.uri']})"
            
        )
        # iterate over every row and create an APA entry
        for i, row in dfToCite.iterrows()


    ]

    print(dfToCite.head())

    dfToCite.to_csv('cleaned_csv.csv')

