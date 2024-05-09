# Nested if else : When you want to go in next step after the previous condition fulfilled.

pre,mains,criteria=92,90,95
if pre>=criteria and pre<=100:
    if mains>=criteria and mains<=100:
        print("You are selected to Interview process")
    else:
        print(f"Your mains score {mains} is less than criteria={criteria}")
else:
    print(f"Your pre score is {pre} is less than criteria={criteria}")
