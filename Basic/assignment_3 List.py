# Q.1 WAP to get count of even numbers between 1 and 100.
even = 0
for number in range(1, 101):
    if number % 2 == 0:
        even = even + 1

print(f"count of even numbers is {even}")

print("----------------------- Q. 1 -------------------------")

# Q.2 WAP to get count of even and odd  numbers between 1 and 50.
even = 0
odd = 0
for number in range(1, 51):
    if number % 2 == 0:
        even  = even + 1
    else:
        odd = odd + 1
print(f"Count of even numbers is {even}")
print(f"Count of odd numbers is {odd}")


print("--------------------- Q. 2 ---------------------------")

# Q.3 WAP to get sum of even and odd  numbers between 1 and 100.
sum_of_even = 1
sum_of_odd = 1
for i in range(1, 101):
    if i % 2 == 0:
        sum_of_even = sum_of_even + i
    else:
        sum_of_odd = sum_of_odd + i
print(f"Sum of even numbers is {sum_of_even}")
print(f"Sum of odd numbers is {sum_of_odd}")


print("--------------------- Q. 3 ---------------------------")

# Q.4 WAP to get average of even and odd  numbers between 1 and 100.

lst1 = []
lst2 = []
for i in range(1, 101):
    if i % 2 == 0:
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1)
print(lst2)
# print average of sum numbers
average_of_sum_numbers = sum(lst1) / len(lst1)
print(average_of_sum_numbers)

# print average of odd numbers
average_of_odd_numbers = sum(lst2) / len(lst2)
print(average_of_odd_numbers)

print("--------------------- Q. 4 ---------------------------")

# Q.5 WAP to get count of numbers between 1 and 100 which is divisible by 7.
count = 0
for number in range(1,101):
    if number % 7 == 0:
        count = count + 1

print(f"Count = {count}")


print("--------------------- Q. 5 ---------------------------")

# Q.9
data = ["indore", "ujjain", "bhopal", "devash", "jabalpur"]
for city in data:
    print(city.upper())

print("------------------- Q. 9 -----------------------------")

# Q.10
data = ["Indore", "Ujjain", "Bhopal", "Devash", "Jabalpur"]
data[0] = "Clean city"
print(data)

print("----------------- Q. 10 -------------------------------")

