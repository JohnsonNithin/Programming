# Lambda functions:
z=lambda x:x**3
print(z(3))

# map
# map(function, iterable)

L=[1,2,3,4,5,6,7,8,9,10]
map(lambda x:x*2,L)
print(list(map(lambda x:x*2,L)))


# filter
# filter(function, iterable)

L=[1,2,3,4,5,6,7,8,9,10]
filter(lambda x:x%2==0,L)
print(list(filter(lambda x:x%2==0,L))) # prints even numbers in the list

# reduce
# reduce(function, iterable)

from functools import reduce
L=[1,2,3,4,5,6,7,8,9,10]
reduce(lambda x,y:x+y,L)
print(reduce(lambda x,y:x+y,L)) # prints the sum of all the elements in the list

print(reduce(lambda x,y:x if x>y else y,L)) # prints the maximum number in the list

