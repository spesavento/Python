import pandas as pd
import re #regular expressions

#load in a dataframe
df = pd.read_csv("Pokemon.csv")

#Other formats
#df_txt = pd.read_csv("Pokemon.txt", delimiter = '\t') tab separated instead of comma separated
#df_xlsx = pd.read_excel("Pokemon.xlsx")

#load in excel files 
print(df.head()) #default 5
print(df.tail(3))

#All the column names
print(df.columns)  #index to get specfic columns
#Print a column
print(df['Name'])
print(df['Name'][0:5]) #row 0 up to 5
print(df[['Name', 'Type 1', 'HP']][0:5]) #list

#Print a row
print(df.iloc[0:3]) #row 0 up to 3

#Print a cell
print(df.iloc[2,1]) #row 0 up to 3

#iterate through each row
#for index, row in df.iterrows(): 
#    print(index, row) or print(index, row['Name'])

#find data (iloc is index)
print(df.loc[df["Type 1"] == "Fire"].head())

print(df.describe())

#sort
print(df.sort_values('Name'))
print(df.sort_values('Name', ascending=False))
print(df[['Name', 'Type 1', 'HP']].sort_values(['Type 1', 'HP']))
print(df[['Name', 'Type 1', 'HP']].sort_values(['Type 1', 'HP'], ascending=[1,0]))#asc desc

#create new columns - long style
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def']+ df['Speed']
print(df.head())

#drop a column
df = df.drop(columns = 'Total')
print(df.head())

#add a column - better way [] 
#sum columns 4 through 9, .sum(axis=1) is summing horizontally, 0 would be vertically
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

#change column ordering
cols = list(df.columns)
print(cols)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head())

#save a csv
#df.to_csv("modified.csv", index = False)  #index = False means there is no first column with indeces
#df.to_excel("modified.xlsx", index = False)
#df.to_csv("modified.txt", index = False, sep = '\t')   seperates it with tabs rather than commas

#inside pandas use & |
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(new_df)
#reset the indeces, 
new_df.reset_index(drop = True, inplace = True) #gets rid of old 'index' column, inplace = True means you don't have to do set it equal to new_df again 
print(new_df)

#filter to get names with 'Mega' anywhere in them use column.str.contains()
mega_df = df.loc[df['Name'].str.contains('Mega')].head()
print(mega_df)
notmega_df = df.loc[~df['Name'].str.contains('Mega')].head()
print(notmega_df)
# ~ is NOT 
# flags = re.I  is ignore the case of the words
regex_df = df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex = True)].head()
print(regex_df)

# ^ start of line  * is any
regexPi_df = df.loc[df['Name'].str.contains('^pi*', flags = re.I, regex = True)].head()
print(regexPi_df)

#.loc[ row is Fire, column Type 1] set all these to Flamer or change back
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df.head())
df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'

#all fire pokemon are legendary
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
print(df.head())

df.loc[df['Total'] > 400, ['Generation', 'Legendary']] = 'TEST VALUE'
print(df[['Name', 'Total', 'Generation', 'Legendary']].head())
df.loc[df['Total'] > 400, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']
print(df[['Name', 'Total', 'Generation', 'Legendary']].head())

#reset
df = pd.read_csv("Pokemon.csv")


#GROUP BY
print(df.groupby(['Type 1']).mean()) #find the mean of the other columns BY Type 1
print(df.groupby(['Type 1']).mean().sort_values('Total', ascending = False)[['Total', 'HP']]) #find the mean of the other columns BY Type 1

print(df.groupby('Type 1').count())

df['count'] = 1 #create your own column because .count() doesn't count blanks
print(df.groupby(['Type 1', 'Type 2']).count()['count'])

#loads the dataframe in chunks of 5
for df in pd.read_csv("Pokemon.csv", chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])  #concats whole data frame with a dataframe 
    
print(new_df)

new_df.info()

