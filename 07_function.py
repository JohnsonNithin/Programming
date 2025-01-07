# write a function that takes variable number of arguments and returns their sum.
def sum_all(*args): # *args takes multiple parameters and stores them in a tuple
    print(sum(args)) # but when you call the sum of args put without asterik, it will give you the sum of the tuple

a=sum_all(1,2,3,4,5,6,7,8,9,10)
