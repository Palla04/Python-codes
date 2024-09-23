from collections import Counter
import string

# Function to count word frequency from a text file
def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_count = Counter(words)

    return word_count

# Main logic
if __name__ == "_main_":
    # File path for the text file
    file_path = 'input.txt'  # Replace 'input.txt' with the path to your text file

    # Get the word frequency
    word_count = count_word_frequency(file_path)

    # Print the word frequency
    for word, freq in word_count.items():
        print(f"{word}: {freq}")