from itertools import permutations

def generate_all_strings():
    count=0
    characters = ['a', 'e', 'i', 'o', 'u']

    all_permutations = permutations(characters)
    
    # Print each permutation as a joined string
    for p in all_permutations:
        count+=1
        print(''.join(p))
    
    print(count)

generate_all_strings()
