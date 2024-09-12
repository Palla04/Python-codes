import re

def an_before_vowel(sentence):
    # Regular expression to remove punctuation and split into words
    words = re.findall(r'\b\w+\b', sentence.lower())

    vowels = ('a', 'e', 'i', 'o', 'u')

    # Loop through the words to check "an" followed by a vowel-starting word
    for i in range(len(words) - 1):
        # If the word is "an"
        if words[i] == 'an':
            # Ensure the next word starts with a vowel
            if words[i + 1][0] not in vowels:
                return False
        
        # If the word is "a"
        if words[i] == 'a':
            # Ensure the next word does not start with a vowel
            if words[i + 1][0] in vowels:
                return False

    return True

sentence = "This is an example of an interesting idea."

if an_before_vowel(sentence):
    print("Correct")
else:
    print("Incorrect")
