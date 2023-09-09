import time

tasks = []


def addTask(task):
    tasks.append(task)
    time.sleep(1)
    print(f"Task {task} added")


def deleteTask(task:int):
    try:
        if tasks[task - 1]:
            tasks.remove(tasks[task - 1])
            time.sleep(1)
            print('Task deleted')
        else:
            print('You do not have this task')
    except Exception as e:
        print('Something went wrong')

def showTasks():
    print('Tasks to do: ')
    for i, j in enumerate(tasks):
        print(f'{i + 1}. {j}')
        time.sleep(1)


while True:
    choice = int(input(('\nWhat do you want to do: \n1. Add task\n2. Delete task\n3. Show all the tasks\n4. Exit\n')))

    if choice == 1:
        time.sleep(1)
        task = input("Enter new task: ")
        addTask(task)
    elif choice == 2:
        time.sleep(1)
        task = int( input('Enter the number of your task: '))
        deleteTask(task)
    elif choice == 3:
        time.sleep(1)
        showTasks()
    elif choice == 4:
        print('Thanks for using us. See ya later!')
        break
    else:
        print("Invalid choice")