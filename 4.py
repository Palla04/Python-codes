import re

def an_before_vowel(Sentence):
    vowels = ('a','e','i','o','u')

    words = Sentence.lower().split()

    for i in range(1,len(words)):
        if words[i].startswith(vowels):
            if words[i-1] != 'an':
               return False
    
    return True

Sentence = "This is an example of an interesting idea."

if an_before_vowel(Sentence):
    print("correct")
else:
    print("Incorrect")