# lambda function : anonymous function
# without name of function we can use ( sort cuts )
def addition(a, b):
    sum  = a + b
    return sum
print(addition(10,20))

# arguments : n numbers , expression only one
# addition by lambda function
sum = lambda a, b: a + b
print(sum(10,20))
print(sum(22, 22))

# Calculate the area of circle
area = lambda radius: 3.14 * radius**2
print(area(10))

# Q1. Create a lambda function to calculate simple interest.
b = lambda p, r, t: (p*r*t)/100
print(b(1000, 5, 2))

# apply multiple conditions in lambda function
# maximum number
max_number = lambda n1, n2 : n1 if n1 > n2 else n2
print(max_number(10, 5))

# Q2. Create a lambda function to check number is  even or odd.
s = lambda num: "even" if num % 2 == 0 else "odd"
print(s(12))

# Calculate square of each number in a list
# map() : apply a function to each element of collection
data = [1, 2, 3, 4, 5]
square = lambda n : n**2
print(list(map(square, data)))

# Q3. Use map() function and lambda function to calculate the cube of each element in a given list.
data = [1,2,3,4,5]
cube = lambda num : num**3
print(list(map(cube, data)))

# filter() : to filter the element of a sequence based on the condition
print(list(filter(lambda num : num > 3, data)))

# get even numbers
print(list(filter(lambda num : num % 2 == 0, data)))

# reduce() : return single value
# import reduce function
from functools import reduce
# addition of each element in a sequence by reduce function
print(reduce(lambda a, b : a + b, data))

# multiplication of each element in a sequence by reduce function
print(reduce(lambda a, b : a*b, data))


# Convert the data in a given list into capital latter's.
data = ["ajay", "raghav", "akhilesh", "pooja", "shivani", "virat"]
name = lambda x : x.upper()
print(list(map(name, data)))



