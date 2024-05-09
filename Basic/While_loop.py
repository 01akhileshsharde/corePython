# While loop : Conditional loop

jabTakHaiJan = True  # it is a infinite loop
round = 0    # externally stop the variable
while(jabTakHaiJan):
    round = round + 1
    print("Basanti will dance",round)
    if(round>=500):  # given a condition for loop
        jabTakHaiJan=False   # stop loop after if condition
else:
    print("Outside  While loop")
