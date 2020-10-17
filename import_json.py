import pandas as pd

df = pd.read_csv('char_dictionary.csv' ,sep=';')
char = df.loc[df['number'] == 2].values[0,1]
print(char)