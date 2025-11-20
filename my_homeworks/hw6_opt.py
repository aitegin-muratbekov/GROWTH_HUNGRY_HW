tasks = []
while True:
    answer = input("Menu \n Add new task: 1\n View tasks:2\n remove task:3\n quit: q \n")
    if answer == '1':
        task = input("What kind of task?\n")
        with open("tasks.txt", "a") as f:
            f.write(f"{task}\n")
        tasks.append(task)
        f.close()
    elif answer == '2':
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            for task in lines: 
                print(f"{lines.index(task)+1}. {task} \n", end='')
        f.close()
    elif answer == '3':
        option = str(input("index or name?\n"))
        if option.isdigit() == True:
            del tasks[int(option)-1]
        else:
             tasks.remove(option)

        with open('tasks.txt', "w") as f:
            for line in tasks:
                    f.write(line)
        
    elif answer == "q":
        print("BYE!")
        break
    else: 
        print("Wrong option")
        continue