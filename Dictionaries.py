# Dictionaries store a mapping between a set of keys and set of values

d = {'user':'Pallabi', 'pswd':1245, 'email':'hello@gmail.com'}
print(d['user'])
print(d['pswd'])
        # print(d['Pallabi'])   traceback not possible

# To change value
d['user'] = 'Riya'
print(d)

# To insert another key with value
d['id']=45
print(d)

# keys()
print(d.keys())

# Item()
print(d.items())

# Del() 
del(d['user'])
print(d)

# clear()
# d.clear()
# print(d)

# Show all keys and values with specific format:
for k in sorted(d.keys()):
  print('key:',k,'->',d[k])
