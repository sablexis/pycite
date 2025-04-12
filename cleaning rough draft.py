import re
import pandas as pd

uncleanedCSV = pd.read_csv('source data/Undergraduate Theses Mar 3 2025.csv')

#  make a copy as to not destroy our original data

cleanedCSV = uncleanedCSV.copy()

cleanedCSV.head()

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

# slapping empty cols to the end of this dataset 
# uncleanedCSV['contributor.first'] = None
# uncleanedCSV['contributor.lastI'] = None
# uncleanedCSV['contributor.middleI'] = None



print(cleanedCSV[['dc.contributor.author']])


# lets get the strings from these cols
for i, name in cleanedCSV[['dc.contributor.author']].iterrows():
    print(name["dc.contributor.author"]) 

# split at the comma
nameParts = name.str.split(', ')

cleanedCSV[['dc.contributor.author.last', 'dc.contributor.author.first']] = cleanedCSV['dc.contributor.author'].str.split(',', expand=True)

# strip our names of trailing whitespaces for easier use later
cleanedCSV['dc.contributor.author.last'] = cleanedCSV['dc.contributor.author.last'].str.strip()
cleanedCSV['dc.contributor.author.first'] = cleanedCSV['dc.contributor.author.first'].str.strip()

print(cleanedCSV['dc.contributor.author.last'])

print(cleanedCSV['dc.contributor.author.first'])

print(cleanedCSV.columns)

# get the inital of the first name incase we need it for certain citations

# creating a column of all the first names in the dataframe
firstNames = cleanedCSV['dc.contributor.author.first']

# created the initals column and get that firstNames data in there
cleanedCSV['dc.contributor.author.first.inital'] = firstNames.str[0]

print(cleanedCSV['dc.contributor.author.first.inital'])


"""
.+:  matches one or more of any character (except newline characters)
(.): This is a capturing group. It matches any single character (except newline) immediately before the period. The parentheses make it a capturing group so str.extract will return only the captured character.
\.: This matches a literal period. The backslash \ is used to escape the period, because a period on its own has special meaning in regex.
"""
regex = r".+(.)\."

# since our firstNames column is already striped for us, we'll use it again
cleanedCSV['dc.contributor.author.middle.inital'] = firstNames.str.extract(regex)

print(cleanedCSV['dc.contributor.author.middle.inital'])

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
for ind, row in cleanedCSV.iterrows():
    name = row['dc.contributor.author.first']

    if '.' not in name:  # if there's no period lets not even do any regex, just leave it be
        continue
    match = re.search(regexForFirsts, name)  # Use re.search to find the match

    if match:
        justNames = match.group(1)  # Extract the captured group
        cleanedCSV.loc[ind, 'dc.contributor.author.first'] = justNames # update our first name list with the correct names now

# creating a column of all the first names in the dataframe
lastNames = cleanedCSV['dc.contributor.author.last']

# created the initals column and get that firstNames data in there
cleanedCSV['dc.contributor.author.last.inital'] = lastNames.str[0]

print(cleanedCSV.iloc[0])


print(cleanedCSV.head())




    # if after comma, grab first letter of last name
    # pipe into column, first inital column 
    # pipe into column, last inital column 



# shortenNames(contributorAuth)
