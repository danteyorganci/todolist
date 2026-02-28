#r
#a
#w
#x

def inside():
    f = open("list/tasks1.txt", encoding="utf-8")
    print("Tasks:")
    print(f.read())


def add():
    ques = input("Would you like to add a task? y/n")
    if ques.lower() == "y":
        added = input("Type in the task you would like to add?")
        f = open("list/tasks1.txt", "a", encoding="utf-8")
        f.write(added + "\n")
    else:
        return

def done():
    # Load tasks from file
    with open("list/tasks1.txt", "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file]

    # Show tasks with numbers
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    # Ask which task to delete
    num = int(input("Enter the number of the task to delete: "))
    tasks[num-1] = "✅ " + tasks[num-1] # removes that one task

    # Save the updated list back to the file
    with open("list/tasks1.txt", "w",encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

    print("Task marked as done!")    


def delete():
    # Load tasks from file
    with open("list/tasks1.txt", "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file]

    # Show tasks with numbers
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    # Ask which task to delete
    num = int(input("Enter the number of the task to delete: "))
    tasks.pop(num - 1)  # removes that one task

    # Save the updated list back to the file
    with open("list/tasks1.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

    print("Task deleted!")

def menu():
    while True:
        with open("list/tasks1.txt", encoding="utf-8")as file:
            content = file.read()

        if not content:
            print("You have no tasks")
        print("what would u like to do? ")
        print("A : Add a new task")
        print("B : Delete a task")
        print("C : Mark a task as done")
        print("D : Read my tasks")
        print("F : Exit")
        choice = input("Choose an option: ").upper()

        if choice == "A":
            add()
        elif choice == "B":
            delete()
        elif choice == "C":
            done()
        elif choice == "D":
            inside()
        elif choice == "F":
            confirm = input("Are you sure? y/n ")
            if confirm.lower() == "y":
                break
            else:
                continue
menu()
