from itertools import permutations

def generate_all_strings():
    characters = ['a', 'e', 'i', 'o', 'u']

    all_permutations = permutations(characters)
    
    # Print each permutation as a joined string
    for p in all_permutations:
        print(''.join(p))

generate_all_strings()
