import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_data = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter something: ").upper()
output_list = [phonetic_data[letter] for letter in name]
print(output_list)
