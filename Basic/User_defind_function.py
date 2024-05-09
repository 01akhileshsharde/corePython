# In-build function : print, len, max, min, etc
# User defined function : we can create a function to perform specific task


# based on return type
# with return type
# without return type

# Based on Argument:
# Relative argument
# Keyword argument
# default argument
# variable length argument(varargs)

# without return type and without arguments
def printHello():
    print("Hello to all")
    return   # optional

# printHello()

# without return value with argument
def printName(name):
    print(f"Hello {name}")

printName("Akhilesh")


# with return type with argument
def addition(a, b):
    sum=a + b
    return  sum

result = addition(5,10)
print(result)

print(addition(5,10))

