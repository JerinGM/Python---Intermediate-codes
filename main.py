# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas
dataformat_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(dataformat_csv)
new_dict = {row.letter: row.code for (index, row) in dataformat_csv.iterrows()}
print(new_dict)
inputFromUser = input("Enter a word: ")
i = inputFromUser.upper()
output = [new_dict[letter] for letter in i]
print(output)