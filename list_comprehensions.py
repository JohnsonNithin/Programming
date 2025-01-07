L = [1,2,3,4,5,6,7]
# listcomprehension syntax: [expression for item in list if condition]
print([x+1 for x in L ])

L = [1,2,3,4,5,6,7]
print([x*2 for x in L if x%2==0]) # charting out the even numbers and muliplying with 2 for the even numbers