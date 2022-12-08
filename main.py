import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)
code_dict = {row.letter: row.code for (index,row) in df.iterrows()}
print(code_dict)




#TODO 2. Phonetic from user input


