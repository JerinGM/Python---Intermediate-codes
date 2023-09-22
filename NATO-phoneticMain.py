
import pandas
dataformat_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(dataformat_csv)
new_dict = {row.letter: row.code for (index, row) in dataformat_csv.iterrows()}
print(new_dict)


def recall():
    inputFromUser = input("Enter a word: ")
    i = inputFromUser.upper()
    try:
        output = [new_dict[letter] for letter in i]
    except KeyError:
        print("Sorry, enter a word")
        blah()
    else:
        print(output)

recall()