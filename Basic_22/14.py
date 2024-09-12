def divisible_by_5(binary_nums):
    arr = []
    for i in binary_nums:
        decimal_value = int(i, 2)  # Convert binary to decimal

        if decimal_value % 5 == 0:
            arr.append(i)  

    return arr

numbers = input("Enter 4-digit binary numbers separated by commas: ")

binary_nums = numbers.split(",")
result = divisible_by_5(binary_nums)
                        
print("Numbers that are divisible by 5:", result)
