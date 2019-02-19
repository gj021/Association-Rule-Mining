import pandas
import pickle
import math
import numpy as np
# data=pd.read_csv('groceries.csv', error_bad_lines=False)

# Input
data_file = "groceries.csv"

# Delimiter
data_file_delimiter = ','

# The max column count a line in the file could have
largest_column_count = 0

# Loop the data lines
with open(data_file, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(data_file_delimiter)) + 1

        # Set the new most column count
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

# Close file
temp_f.close()

# Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
column_names = [i for i in range(0, largest_column_count)]

# Read csv
df = pandas.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)
# print(df[0][1])

items={}

df = df.fillna('')

df=df.values

print(df[0][0])

size=df.shape

print(size)



for i in range(size[0]):
	for j in range(size[1]):
		if (df[i][j] not in items) and (df[i][j]!=''):
			l = []
			l.append(i)
			items[df[i][j]] = l 
		elif df[i][j]!='':
			l=items[df[i][j]]
			l.append(i)
			items[df[i][j]]=l

output=open("./pkl_files/items.pkl",'wb')
pickle.dump(items,output)
output.close()

print(items)

