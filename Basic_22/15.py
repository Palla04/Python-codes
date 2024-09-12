def count_letter_digit(sentence):

    letter_count=0
    digit_count=0

    for i in sentence:
        if i.isalpha():
            letter_count+=1
        elif i.isdigit():
            digit_count+=1

    return letter_count, digit_count


sentence = input("Enter the string: ")
letter, digit = count_letter_digit(sentence)
print("Number of letters : ",letter, "Number of Digit: ", digit)