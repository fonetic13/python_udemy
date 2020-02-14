import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_word(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), n=1)) > 0:
        print("Did you mean %s?" % get_close_matches(word, data.keys(), n=1)[0])
        response = input("Type Y for yes or N for no: ")
        if response == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word doesn't exist, please double check it!"
    else:
        return "Word doesn't exist, please double check it!"

word = input("Please enter word: ")

output = find_word(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
