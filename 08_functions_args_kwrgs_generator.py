# function with *args

def deq(*args): # takes multiple arguments and stores them in a tuple
    for i in args:
        print(i)
deq(1,2,3,4,5,6,7,8,9,10,11,12)# takes multiple arguments and stores them in a tuple




 # function with *kwargs
def dq(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}:{value}")   


print(dq(name='Nithin', age='32',job='Data Scientist')) # takes multiple keyword arguments and stores them in a dictionary


#Yield

# keeps the state of the function and resumes from where it left off and memory efficient
L=[]
def even_generator(num):
    for i in range (1,num+1):
        if i %2==0:
             L.append(i)
    return L


print(even_generator(10))
