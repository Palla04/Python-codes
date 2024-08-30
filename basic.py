from fractions import Fraction
import math

a=7
print(a)
b='Hello World'
print(len(b))

# String add
name="Pallabi"
name=name+'!!!'
print("Hello", name)

d = """a'b"c"""
print(d)

print(1j*1j)

# Special Function
print(Fraction(4,6))
print(math.pi)
print(Fraction('.25'))

x,y,z=1,3,7
print(x)
print(y)
print(z)

# Lists, Tuples
tuple = (23,'abc',4.56,(2,3),'def')
print(tuple[3])
print(tuple[-3])
# tuple[2]=4   As tuples is not Mutable

list = ["abc",34,4.34,'ab']
print(list[1:3])
print(list[:3])
list[2]=2
print(list) #As Lists is Mutable 

# copy of a list
list_1 = list
print(list_1)

# in operation
array = [1,2,3,5]
print(4 in array)

a = 'Hello'
print('c' in a)
print('l' in a)

# + and * operator
arr_1 = (1,2,3)+(4,5,6)
print(arr_1)
p = 'Hello'+' '+'World'
print(p)

arr_2 = (1,2,3)*3
print(arr_2)
