import json
import difflib


iword = input("Enter word: ")
words = json.load(open("data.json"))

def search_key(search_val):
    search_val = search_val.lower()
    if search_val in words:
        return(words[search_val])
    else:
        dym = get_close_match(search_val, words.keys(), n=1)
        return f"Did you mean {dym}? Y or N?:"

print(search_key(iword))
