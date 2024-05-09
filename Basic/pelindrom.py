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

def prime_number(num):
    if num == 1:
        return "Not prime"
    else:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not prime"
                break
            else:
                return f"{num} is prime"

print(prime_number(9))