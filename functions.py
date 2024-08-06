


# Let's define a function in Python
# Define a function that multiplies any number by 10
def multiply_by_10(num):
    return num * 10

result = multiply_by_10(32)
print(result)


# Define a function that adds two numbers together
def sum(a,b):
    return a + b

print(sum(10,32))

# sum(10) # <-- runtime error! Error is thrown during execution of the program
# TypeError: sum() missing 1 required positional argument

def sum_list(list):
    total = 0 ## <-- initialise sum
    for item in list:
        total += item
    return total

print(sum_list([1,2,3,4,5,6,7,8,9,10]))
# print(total) # <-- NameError: name 'total' is not defined
# total is defined in the scope of sum_list

def map(list, f):
    return [f(x) for x in list]

# list comprehension allows us to apply a function f to each element x in list

print(map([1,2,3,4],lambda x: x * 5))
# lambda is a function we can pass through as an argument to our map function
# map is higher order function as it accepts an argument

 
name = 'mitch'
letters = [char for char in name]
print(letters)


def identity(x):
    return x

list = [1,2,3]
result = identity(list)
print(hex(id(list)),'<----- prints the hexadecimal memory address of list')

def no_op():
    return


print(no_op())

