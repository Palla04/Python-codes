# Append, Insert, Extend operation on List

li = [1,11,3,5]

li.append('a')
print(li)

li.insert(2,9)
print(li)

li.extend([9,10,20])
print(li)

# extend vs append

print()
li_1 = [2,4,6]
print(li_1)
li_1.append([9,10,20])
print(li_1)

print()

li_1.extend([9,10,20])
print(li_1)


# Operation on List (Index, Count, Remove)

print()
li_3 = ['a','b','c','b']
print(li_3)
print(li_3.index('b'))
print(li_3.count('b'))
li_3.remove('b')
print(li_3)

# Operation on List (Reverse, Sort)
li_4 = [5,2,7,9]
li_4.reverse()
print(li_4)

li_4.sort()
print(li_4)

