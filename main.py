from difflib import get_close_matches
import json

data = json.load(open("Dictionary/dictionary.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y for yes and n for no"%get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n':
            return "Word doesnt Exist Please Check the spelling."
        else:
            return "We did not understand your entry."
    else:
        return "The Word does not exist"

p = input("Enter the word: ")

output = translate(p)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)