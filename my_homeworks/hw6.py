import random

random_n = random.randint(1, 5)
counter = 0

a = int(input("Try to guess the number from 1 to 100 \n"))
 
while counter < 3:
    if counter >= 1:
        a = int(input("Try guess it again"))

    if a > random_n:
        print(f"{a} is to high")
    elif a < random_n:
        print(f"{a} is too low")
    else:
        print ("You guess it!!")
        break
    counter +=1
else:
    print("Attempts: 0")

   

