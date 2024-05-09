# Different pattern by for loop

for row in range(1,6):
    for col in range(1,6):
        print(col,end=" ")
    print()

# output
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
'''

print("-------------pattern 1-------------")


for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()

print("------------pattern 2-------------")


for row in range(1,6):
    for col in range(1,6):
        print(row,end=" ")
    print()

# output
'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''

print("------------pattern 3------------")


for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

# output
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

print("----------pattern 4--------------")


for row in range(1,6):
    for col in range(1,row+1):
        print(row,end=" ")
    print()

# output
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

print("-----------pattern 5-------------")


# reverse pattern
for row in range(1,6):
    for col in range(5,row-1,-1):  # 5 4 3 2 1 [5:0:-1]
        print(col,end=" ")
    print()

# output
'''
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
'''

print("------------pattern 6-------------")


for row in range(5,0,-1):    # row in decremented order
    for col in range(1,row+1):   # columns in incremented order
        print(row,end=" ")
    print()

# output
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

'''
print("-------------pattern 7--------------")

a = 65
for i in range(1,6):
    for j in range(1,6):
        # chr() : convert number to character
        print(chr(a), end=" ")
    print()

# Output:
'''
A A A A A 
A A A A A 
A A A A A 
A A A A A 
A A A A A 
'''



print("------------Pattern 8----------------")


a = 65
for row in range(1,6):
    a =65
    for space in range(5,row,-1):
        print(" ",end=" ")
    for col in range(1, row+1):
        print(chr(a),end=" ")
        a = a+1
    print()
# Output:
'''
        A 
      A B 
    A B C 
  A B C D 
A B C D E
'''

print("--------------pattern 9------------")


for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end=" ")
    for col in range(1, row+1):
        print(row,end=" ")
    print()
# Output
'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5
'''

print("--------------pattern 10--------------")

for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end=" ")
    for col in range(1, row+1):
        print(col,end=" ")
    print()
# Output
'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
'''

print("-----------Pattern 11-----------------")


for row in range(5,0,-1):
    for space in range(5,row,-1):
        print(" ",end=" ")
    for col in range(1, row+1):
        print(row,end=" ")
    print()
# Output
''''
5 5 5 5 5 
  4 4 4 4 
    3 3 3 
      2 2 
        1 

'''

print("--------------pattern 12---------------")