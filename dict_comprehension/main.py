import json


# Input prompt
word = input("Give a word: ").upper()

# Count the frequency of each character
number_of_letters = {}

for char in word:
    if char in number_of_letters.keys():
        number_of_letters[char] += 1
    else:
        number_of_letters[char] = 1


# Construct the output dictionary
word_dict = [
        {"word": word.title()},
        {"letters": len(word)},
        number_of_letters
]

# Pretty-print the JSON output
print(json.dumps(word_dict, indent=4))
