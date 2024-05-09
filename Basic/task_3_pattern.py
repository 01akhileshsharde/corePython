for row in ('A','B','C','D','E'):
    for col in ('A','B','C','D','E' ):
        print(row,end=" ")
    print()

# output
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
'''

print("------------------")

for row in range(1,6):
    for col in range(1,row):
        print(col,end=" ")
    print()