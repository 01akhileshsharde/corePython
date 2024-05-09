# Else_self_ladder
# When you have more than 1 condition
# Only if : When you are intrested in true

budget=int(input("Enter your Budget\n"))
if budget>0 and budget<=500:
    if budget>=400 and budget<=500:
        print("You can buy large size cheese Pizza")
    elif budget>=300 and budget<400:
        print("You can buy medium size cheese Pizza")
    elif budget>=200 and budget<300:
        print("You can buy small size cheese Pizza")
    elif budget>=100 and budget<200:
        print("You can buy Regular  Pizza")
    else:
        print("You can buy Burger above 30 rs.")
else:
    print("Please enter valid amount between 100 and 500")

