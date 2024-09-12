def squre_sum(list):
    sum=0
    for i in list:
        sum += i**2
    
    return sum

list = [1,2,3,4,5]
result = squre_sum(list)
print("Squre Sum is : ", result)