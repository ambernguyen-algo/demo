import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Print information about the entire DataFrame to see which columns need to be cleaned
print(df.info())
# Print information about the entire DataFrame to see which columns need to be cleaned

# How many apps in the dataset have no ('NaN') rating ('Rating')?
print(len(df[pd.isnull(df['Rating'])]))

# Replace the null value ('NaN') of the rating ('Rating') for such apps with -1.
df['Rating'].fillna(-1, inplace = True)

print(df['Size'].value_counts())


def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1
df['Size'] = df['Size'].apply(set_size)


# What is the maximum 'Size' of apps in the 'TOOLS' 'Category'?
print(df[df['Category'] == 'TOOLS']['Size'].max())


# Bonus tasks
# Replace the data type with integer (int) for the number of installs ('Installs').
# In the entry for the number of installs ('Installs'), the “+” sign must be ignored.
# This means that if the number of installs in the dataset is 1,000,000+, you need to change the value to 1000000
def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)


# Group the data by type ('Type') and target audience ('Content Rating') however you prefer,
# calculate the average number of installs ('Installs') for each group. Round the answer to the nearest tenth.
# In the resulting table, find the cell with the largest value.
# What age group and app type does the data in that cell belong to?
print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)


# Which app doesn’t have a 'Type' specified? What type should be entered there depending on the price?
print(df[pd.isnull(df['Type'])])
# You can use iloc[0] to see all the columns instead of the ellipsis.
# print(df[pd.isnull(df['Type'])].iloc[0])
df['Type'].fillna('Free', inplace = True)


# Print information about all the DataFrames to make sure the cleaning is successful
print(df.info())




