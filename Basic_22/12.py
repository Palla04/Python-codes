def make_dic(n):
    d={}
    for i in range(1,n+1):
        d[i] = i*i
    
    return d

n=int(input("Enter the number: "))
result = make_dic(n)
print("the dictionary : ", result)