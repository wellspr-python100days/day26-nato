import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter: row.code for (index, row) in data.iterrows() }

operation_successful = False

while not operation_successful:
    word = input("Enter a word: ").upper()
    
    try:
        list_of_codes = [ nato_dict[letter] for letter in word ]
    except KeyError as key_error:
        print(f"{key_error} is not a valid NATO character.")
    else:
        print(list_of_codes)
        operation_successful = True