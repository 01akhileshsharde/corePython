# function with capital letter
def capitalLetter(*name):
    for i in name:
        print(i.upper())

capitalLetter("Akhilesh", "raghav", "akash")


# check the factorial number
def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        return fact
    else:
        for i in range(1,num+1):
            fact = fact * i
    return fact

print(factorial(3))


# check the pelindrom number
def pelindrom_number(number):
    copy_number = number
    pelindrom = 0
    while(number>0):
        rem = number%10
        pelindrom = pelindrom*10+rem
        number=int(number/10)
    if pelindrom == copy_number:
        print(f"Pelindrom number {copy_number}")
    else:
        print(f"Not pelindrom {copy_number}")

pelindrom_number(1221)


# check prime number
def prime_number(num):
    message = " "
    if num == 1:
        return "Not prime"
    # elif num == 2:
    #   return f"{num} is prime"
    else:
        for i in range(2, (num//2+1)):
            if num % i == 0:
                 message = f"{num} is not prime"
                 break
            else:
               message = f"{num} is prime"
    return message
print(prime_number(2))
