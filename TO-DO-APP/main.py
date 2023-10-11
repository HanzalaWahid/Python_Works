tasks =[]
while True:
        print("TO-DO APP")
        print("1.Add Task")
        print("2.View Task")
        print("3. Completed Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice =="1":
            task = input("Enter the task: ")
            tasks.append(task)
        elif choice =="2":
            for index,task in enumerate(tasks):
                print(f"{index + 1}.{task}")
        elif choice == "3":
            index = int(input("Enter task number to  mark as completed: "))-1
            if 0 <= index < len(tasks):
                print(f"Task'{tasks[index]}'as completed")
                tasks.pop(index)
            else:
                print("Invalid Task number.")
        elif choice == "4":
            index = int(input("Enter task number to  removed: "))-1
            if 0 <= index < len(tasks):
                print(f" Task'{tasks[index]}'as completed")
                tasks.pop(index)
            else:
                print("Invalid Task number.")
        elif choice == "5":
            print("Good Bye!")
            break
        else:
            print("Invalid Choice. Please try again")


