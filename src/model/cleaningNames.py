"""
Name cleaning operations for thesis data

This module contains all functions related to cleaning and processing
thesis name data.

Dependencies:
    - pandas
    - numpy

Author: Sabrina Sandy 
Date: April 12, 2025
"""

# Third-party imports
import re
import pandas as pd
import numpy as np


def clean_theses_data(theses_df):
    """
    Master function that applies all cleaning operations to the theses data
    
    Args:
        theses_df: pandas DataFrame containing the raw theses data
        
    Returns:
        pandas DataFrame: Cleaned theses data
    """

    """
    Chunk out the first, middle and last names into their respective columns 
        
    Paprameters:
        dataframe
        name_col name of the column containing names

    Returns:
        dataframe w added cols
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """

    #  make a copy as to not destroy our original data
    cleanedThesisCSV = theses_df.copy()

    # lets get the strings from these cols
    for i, name in cleanedThesisCSV[['dc.contributor.author']].iterrows():
        print(name["dc.contributor.author"]) 

    # split at the comma
    nameParts = name.str.split(', ')

    cleanedThesisCSV[['dc.contributor.author.last', 'dc.contributor.author.first']] = cleanedThesisCSV['dc.contributor.author'].str.split(',', expand=True)

    # strip our names of trailing whitespaces for easier use later
    cleanedThesisCSV['dc.contributor.author.last'] = cleanedThesisCSV['dc.contributor.author.last'].str.strip()
    cleanedThesisCSV['dc.contributor.author.first'] = cleanedThesisCSV['dc.contributor.author.first'].str.strip()

    # get the inital of the first name incase we need it for certain citations

    # creating a column of all the first names in the dataframe
    firstNames = cleanedThesisCSV['dc.contributor.author.first']

    # created the initals column and get that firstNames data in there
    cleanedThesisCSV['dc.contributor.author.first.inital'] = firstNames.str[0]

    print(cleanedThesisCSV['dc.contributor.author.first.inital'])


    """
    .+:  matches one or more of any character (except newline characters)
    (.): This is a capturing group. It matches any single character (except newline) immediately before the period. The parentheses make it a capturing group so str.extract will return only the captured character.
    \.: This matches a literal period. The backslash \ is used to escape the period, because a period on its own has special meaning in regex.
    """
    regex = r".+(.)\."

    # since our firstNames column is already striped for us, we'll use it again
    cleanedThesisCSV['dc.contributor.author.middle.inital'] = firstNames.str.extract(regex)

    print(cleanedThesisCSV['dc.contributor.author.middle.inital'])

    # now we can update our first names to just the first name, no initals

    """
    ^: Matches the beginning of the str
    (\w+): This is the capturing group that extracts the first name. \w+ matches one or more alphanumeric characters or underscores. We want to capture this, so it's in parentheses.
    (?:\s.+)?: This is a non-capturing group that handles the optional "rest of the name" part.
        \s: Matches a single whitespace character (e.g., a space).
        .+: Matches one or more of any character, this matches the rest of the name (e.g., "D." or "Doe").
        (?: ... ): This creates a non-capturing group. We use this because we don't want to extract the "rest of the name"
        ?: Makes the entire non-capturing group optional. This handles cases where there's only one name
        $: Matches the end of the string.
    """
    regexForFirsts = r"^(\w+)(?:\s.+)?$"

    # iterate over all the rows in our cv
    for ind, row in cleanedThesisCSV.iterrows():
        name = row['dc.contributor.author.first']

        if '.' not in name:  # if there's no period lets not even do any regex, just leave it be
            continue
        match = re.search(regexForFirsts, name)  # Use re.search to find the match

        if match:
            justNames = match.group(1)  # Extract the captured group
            cleanedThesisCSV.loc[ind, 'dc.contributor.author.first'] = justNames # update our first name list with the correct names now

    # creating a column of all the first names in the dataframe
    lastNames = cleanedThesisCSV['dc.contributor.author.last']

    # created the initals column and get that firstNames data in there
    cleanedThesisCSV['dc.contributor.author.last.inital'] = lastNames.str[0]

    print(cleanedThesisCSV.iloc[0])


    print(cleanedThesisCSV.head())



    cleanedThesisCSV.to_csv('cleaned_csv.csv')