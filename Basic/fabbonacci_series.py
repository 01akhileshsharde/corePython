def fabbonacci_series(number):
    number = int(input("Enter a number: "))
    n1 = 0
    n2 = 1
    n3 = 0
    print(n1, " , ", n2)
    for i in range(number):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
fabbonacci_series(5)