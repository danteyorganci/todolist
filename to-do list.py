# A clean and updated vesion of my original to-do list
import os

def confirm():
    ques = input("Are you sure? y/n ")
    if ques.lower() == "y":
        return True
    else:
        print("You have not writen, y.")
        return False


if not os.path.exists("list/tasks1.txt"):               # Makes the file if not already existing
    open("list/tasks1.txt", "w", encoding="utf-8").close()

def inside():
    with open("list/tasks1.txt", encoding="utf-8") as f:
        print(f.read())

def add():
    ques = input("Would you like to add a task? y/n ")
    if ques.lower() == "y":
        added = input("Type in the task you would like to add? ")
        conf = input(f"Are you sure you want to add '{added}' to your Tasks? y/n ")
        if conf.lower() == "y":
            fi = open("list/tasks1.txt", "a", encoding="utf-8")
            fi.write(added + "\n")
            fi.close()
            print("Task added!")
        else:
            print("You have not writen, y.")
            return
    else:
        return

def done():
    # Load tasks from file
    with open("list/tasks1.txt", encoding="utf-8") as f:
        tasks = [line.strip() for line in f] # Cut out weird stuff like \n at the end of lines

    # Show tasks with numbers
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    # Ask which task to delete
    num = int(input("Enter the number of the task to finish: "))
    tasks[num-1] = "✅ " + tasks[num-1] # Makes the task have a tick at the start

    # Save the updated list back to the file
    with open("list/tasks1.txt", "w",encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

    print("Task marked as done!")    


def delete():
    with open("list/tasks1.txt", "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file]

    if not tasks:
        print("No tasks to delete.")
        return

    while True:
        # Show tasks
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        try:
            num = int(input("Enter the number of the task to delete: "))
            if num < 1 or num > len(tasks):
                print("Invalid task number.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        if confirm():
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Cancelled.")

        again = input("Delete another task? y/n ").lower()
        if again != "y":
            break

    # Save updated list
    with open("list/tasks1.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
            
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
            EXIT_confirm = input("Are you sure? y/n  ")
            if EXIT_confirm.lower() == "y":
                break
            else:
                continue
menu()
