# Set is a collection of unique value
# It is a unordered collection of value

# Empty set
s = set()  # using set constructor
print(type(s))

# Single value set
s1 = {1}
print(type(s1))

s2 = {1,2,3,4,5,1,2,6,2,5,5,6,6}
print(s2)

# add an element in a set
s2.add(20)
print(s2)

# update method - more than 1 element addd in a set
s2.update((7,8,9,11,12,11,14,15,20,22))  # update values as a tuple form
print(s2)

# iterate by for loop
for ele in s2:
    print(ele, end=" ")

# To remove
# pop() method
print(s2.pop())  # remove  1 element start with set (first element)
print(s2)

# remove() method
print(s2.remove(3))  # to remove specified element in a set
print(s2)

# print(s2.clear())  # remove all element

print(s1, "\n", s2)

# difference
print(s2.difference({1,11,2,7,12}))  # common element was remove in difference

print({1,11,2,7,12}.difference(s2))

a = {1,4,7,2,9}
b = {6,1,9,56,23,8}
print(a-b)

# Intersection : keep common element
print(a.intersection(b))

# Union : remove duplicate in both sets
print(a.union(b))

# subset and superset
print(a.issubset(b))
print(b.issubset(b))

print(a.issuperset(b))
print(b.issuperset(a))