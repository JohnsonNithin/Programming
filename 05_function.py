
# Function that greets a user , if no name is provided, it will greet with a default name .

def greet(username='Defaultname'): # the trick is to pass ina avariable with a default value  and if you provide the value along it prints the value
    return username

print(greet('John'))
print(greet())