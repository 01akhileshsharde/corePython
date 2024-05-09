# check number is even with for loop
number = int(input("Enter a number\n"))

if number > 20:
    if number%2 == 0:
        print(f"{number} is even and greater than 20")
    else:
        print(f"{number} is not even but greater than 20")
else:
    print("Please enter a number  greater than 20")
