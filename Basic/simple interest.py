# calculate the simple interest

# convert string to int
principal = int(input("Enter principal amount\n"))
roi = int(input("Enter rate of interest of the principal amount\n"))
time = int(input("Enter time of the principal amount\n"))

si = (principal*roi*time)/100
print(f"The si of = {si}")
