import random

# Q.1) 4 digit OTP generate

print("OTP:")
for i in range(0, 4):
    print(f"{random.randint(0,9)}", end="")

print("\n")

# Q.2) WAP to generate 5 random Number between 0 and 50
for i in range(0, 5):
    print(f"{random.randint(1, 50)} ", end="")

print("\n")

# Q.3) WAP to Generate 6 digit Captcha
print("CAPTCHA:")
data = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwzyz0123456789"
for i in range(0,6):
    print(random.choice(data), end=" ")

print("\n")
'''
Q.4) Guessing game: If user selected number and computer generated number is same:
than user is winner otherwise looser Modify the above game and provide 3 chances to the player 
'''
user = int(input("Please enter a number between 1 to 100 : "))
computer = random.randint(1, 100)
chances = 0
while chances < 3:
    if user == computer:
        print(f" User={user} and computer={computer} than user is winner!")
        break
    else:
        print(f"User={user} and computer={computer} than user is looser!")
        user = int(input("Enter a number between 1 to 100 for new game: "))
        chances = chances + 1
if chances == 3:
    print("Sorry try after some time")