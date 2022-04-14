

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
##print(data)

###Loop through rows of a data frame
##for (index, row) in student_data_frame.iterrows():
##    #Access index and row
##    #Access row.student or row.score
##    pass
##
### Keyword Method with iterrows(er)
### {new_key:new_value for (index, row) in df.iterrows()}
##
###TODO 1. Create a dictionary in this format:
##{"A": "Alfa", "B": "Bravo"}
##
###TODO 2. Create a list of the phonetic code words from a word that the user inputs.
##
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
        
        
