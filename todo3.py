import sqlite3
import time


con = sqlite3.connect('todo.db')
db = con.cursor()
db.execute('CREATE TABLE IF NOT EXISTS tasks(id integer PRIMARY KEY AUTOINCREMENT, task text NOT NULL);')
    



# tasks = []


def addTask(task):
    insert = """INSERT INTO tasks
        (task) 
        VALUES (?);"""
    db.execute(insert, (task, ))
    con.commit()
    time.sleep(1)
    print(f"Task {task} added")


def deleteTask(task:int):
    try:
        delete = """DELETE from tasks where id = ?"""
        if db.execute("SELECT rowid FROM tasks WHERE id = ?", (task, )).fetchone():
            db.execute(delete, (task, ))
            db.execute("SELECT id FROM tasks ORDER BY id")
            rows = db.fetchall()
            for i, row in enumerate(rows, start=1):
                new_id = i
                old_id = row[0]
                if new_id != old_id:
                    db.execute("UPDATE tasks SET id = ? WHERE id = ?", (new_id, old_id))

            con.commit()
            time.sleep(1)
            print('Task deleted')
        else:
            print('You do not have this task')
    except Exception as e:
        print('Something went wrong')

def showTasks():
    print('Tasks to do: ')
    select = """SELECT * from tasks"""
    db.execute(select)
    record = db.fetchall()
    for row in record:
        print(f'{row[0]}. {row[1]}')
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