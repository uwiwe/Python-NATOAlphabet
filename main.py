import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_data)
nato_dict = {row.letter: row.code for index, row in nato_data.iterrows()}

word = input("Type your word: ").upper()
word_list = list(word)
phonetics = [nato_dict[letter] for letter in word_list if letter in nato_dict.keys()]
print(phonetics)