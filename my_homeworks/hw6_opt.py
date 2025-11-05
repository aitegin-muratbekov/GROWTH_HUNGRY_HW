tasks = []

while True:
    answer = input("Menu \n Add new task: 1\n View tasks:2\n remove task:3\n quit: q \n")
    if answer == '1':
        task = input("What kind of task?\n")
        tasks.append(task)
    elif answer == '2':
        for task in tasks:
            print(f"{tasks.index(task)+1}. {task} \n")
    elif answer == '3':
        option = str(input("index or name?\n"))
        if option.isdigit == True:
            del tasks[int(option)+1]
        else:
             tasks.remove(option)
    elif answer == "q":
        print("BYE!")
        break
    else: 
        print("Wrong option")
        continue