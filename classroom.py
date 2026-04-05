#paiton projec

import random, time

class_room = [
    'Max', 'Jan', 'Casey', 'Om', 'Samrat', 'Ikjot', 'Tanmay', 'Aahil', 
    ]

print(class_room)

printed_person = int(input("Who do you want to be printed? : ")) 

if 0 <= printed_person < len(class_room):
    print(class_room[printed_person])
else:
    print(f"Nobody found in index {printed_person}")

time.sleep(0.5)

randomise = input("Would you like to randomly shuffle this list? (y/n) ")

if randomise.lower() in ["y", "yes"]:
    times_shuffled = int(input("How many times more would you like to randomise this list? "))
    
    for i in range(times_shuffled):
        random.shuffle(class_room)
        print(f"Shuffle {i+1}: {class_room}")
        time.sleep(0.3)

    print(f"The shuffled list is: {class_room}")
else:
    print("EOP") 