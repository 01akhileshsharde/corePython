# Relative arguments
def addition(a, b):
    print(f"a = {a}, b = {b}")
    return  a+b

print(addition(2,3))   # automatic fetch value a = 2 and b = 3
print(addition(3,2))


# Variable length argument
def total(*a):
    sum = 0
    for num in a:
        sum = sum + num
    return sum
print(total(1))
print(total(1,2,3))
print(total(1,2,3,4,5,6,7,8,9,10))
