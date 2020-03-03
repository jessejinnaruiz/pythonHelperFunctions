#pd.show_versions()

import pandas as pd
import numpy as np
import re

# pick a file name to import with pandas as a dataframe

# my file has one column called data with the string we want to break up into separate columns
file1 = "Book1.csv"

# read the file using pandas read_csv
csv = pd.read_csv(file1, delimiter=",")

# checking to make sure its a dataframe
#print(type(csv))
print(csv)

# cast the data as string
csv['Data'] = csv['Data'].astype(str)
csv['Data']


# with the dataframe, we are going to split the strings into meaningful columns. first the date
csv['Date'] = csv.Data.str.extract(r'(\d\d[/]\d\d)')

# now the long string in the middle
# regex needs some improvement... this works for now
csv['Expense'] = csv.Data.str.extract(r'( \w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.\w*.)')

# now the total amount
csv['Amount'] = csv. Data.str.extract(r'([0-9]{1,6}[.|,]\d*)')

# checking to see what the dataframe looks like
print(csv)

# output dataframe as a csv file
#csv.to_csv(r'~/Desktop/formatted.txt', sep=',', index=False, header=True)

# output dataframe as a excel file -- looks better
csv.to_excel('formatted.xlsx')