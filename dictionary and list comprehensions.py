L=[1,2,3,4,5,6,7]

# listcomprehension syntax: [expression for item in list if condition]

print([item*2 for item in L])

print([item*3 for item in L if item%2!=0]) # charting out the odd numbers and muliplying with 3 for the odd numbers

fruits=['apple','banana','cherry','kiwi','mango']
# print(fruits[0][0])
print([fruit[0][0].upper() for fruit in fruits if fruit[0]=='a'])
print([fruit[0:].upper() for fruit in fruits if fruit=='apple'])


#DICTANORY COMPREHENSION:
# syntax: {key:value for item in list if condition}

D1= {'name':'Nithin',
    'name1': 'Amala',
    'name2':'Mephalti'}
print(D1)

print([print(value)for value in D1.items()])