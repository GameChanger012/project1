import json
from difflib import get_close_matches

background = json.load(open("data.json"))

def find(word):
    word = word.lower()
    if word in background:
        return background[word]
    elif word.title() in background:
        return background[word.title()]
    elif word.upper() in background:
        return background[word.upper()]
    elif len(get_close_matches(word , background.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, background.keys())[0])
        final = input("y(yes) or n(no)?")
        if final == "y":
            return background[get_close_matches(word , background.keys())[0]]
        elif final == "n":
            return("y for yes or n for no ")
        else:
            return("wrong input please enter just y or n")
    else:
        print(" wrong input")



word = input("Type the word you wish to search here: ")
result = find(word)
if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
