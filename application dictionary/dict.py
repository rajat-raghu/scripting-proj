import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json",'r'))
def search():
    word=input("hello \nplease eneter a word for meaning")
    word= word.lower()
    return word

word=search()

def check(word):
    if word in data:
        return word
    elif len(get_close_matches(word,data.keys(),cutoff=0.7))>0:
        print("did you mean",get_close_matches(word,data.keys())[0],"?")
        ans=input("if yes press 'y' for yes or no press 'n' ")
        print (ans)
        if ans == "y":
            word = get_close_matches(word,data.keys())[0]
            return word
        else:
            print("word dosent exist. Please double check the word you have written ")
            word= search()
            return word    
    else:
        print("word dosent exist. Please double check the word you have written")
        word = search()
        return word
check_word= check(word)

def translate(word):
    return data[word]
word= translate(check_word)
for item in word:
    print(item)
