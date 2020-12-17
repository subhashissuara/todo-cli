# ------------------------------------
#   Author: Subhashis Suara
#   Contact: subhashissuara@gmail.com
#   Note: Python >=3.6 (For f-strings)
# ------------------------------------

import sys
import os.path
from datetime import datetime

class todo():
    # Prints commands & their usage
    def help(self):
        helpMessage = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
        print(helpMessage)
    
    # Prints pending todos in recently added format.
    def ls(self):
        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as todoFileRead:
                tasks = todoFileRead.readlines()
            taskCounter = len(tasks)
            for task in tasks:
                print(f'[{taskCounter}] {task}', end = "")
                taskCounter -= 1
        else:
            print ("There are no pending todos!")
    
    # Adds a new task to todo
    def addTask(self, task):
        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as todoFileRead:
                tasks = todoFileRead.read()
            with open('todo.txt', 'w') as todoFileWrite:
                todoFileWrite.write(f'{task}\n{tasks}')
        else:
            with open('todo.txt', 'w') as todoFileWrite:
                todoFileWrite.write(f'{task}\n')
        print(f'Added todo: "{task}"')
    
    # Deletes a specified task from todo
    def delTask(self, taskNum):
        taskNum = int(taskNum)
        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as todoFileRead:
                tasks = todoFileRead.readlines()
            taskCounter = len(tasks)
            if taskNum <= 0 or taskCounter < taskNum:
                print(f'Error: todo #{taskNum} does not exist. Nothing deleted.')
            else:
                with open('todo.txt', 'w') as todoFileWrite:
                    for task in tasks:
                        if taskCounter != taskNum:
                            todoFileWrite.write(task)
                        taskCounter -= 1
                print(f'Deleted todo #{taskNum}')
        else:
            print(f'Error: todo #{taskNum} does not exist. Nothing deleted.')
    
    # Marks a specified task as done
    def doneTask(self, taskNum):
        taskNum = int(taskNum)
        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as todoFileRead:
                tasks = todoFileRead.readlines()
            taskCounter = len(tasks)
            if taskNum <= 0 or taskCounter < taskNum:
                print(f'Error: todo #{taskNum} does not exist.')
            else:
                with open('todo.txt', 'w') as todoFileWrite:
                    if os.path.isfile('done.txt'):
                        with open('done.txt', 'r') as doneFileRead:
                            tasksDone = doneFileRead.read()
                        with open('done.txt', 'w') as doneFileWrite:
                            for task in tasks:
                                if taskCounter == taskNum:
                                    doneFileWrite.write(f'x {datetime.today().strftime("%Y-%m-%d")} {task}')
                                else:
                                    todoFileWrite.write(task)
                                taskCounter -= 1
                            doneFileWrite.write(tasksDone)
                    else:
                        with open('done.txt', 'w') as doneFileWrite:
                            for task in tasks:
                                if taskCounter == taskNum:
                                    doneFileWrite.write(f'x {datetime.today().strftime("%Y-%m-%d")} {task}')
                                else:
                                    todoFileWrite.write(task)
                                taskCounter -= 1
                print(f'Marked todo #{taskNum} as done.')
        else:
            print(f'Error: todo #{taskNum} does not exist.')
	
    # Generates a report of pending and completed tasks
    def report(self):
        pendingCounter = 0
        doneCounter = 0
        if os.path.isfile('todo.txt'):
            with open('todo.txt', 'r') as todoFileRead:
                tasks = todoFileRead.readlines()
            pendingCounter = len(tasks)
        if os.path.isfile('done.txt'):
            with open('done.txt', 'r') as doneFileRead:
                tasksDone = doneFileRead.readlines()
            doneCounter = len(tasksDone)
        print(f'{datetime.today().strftime("%Y-%m-%d")} Pending : {pendingCounter} Completed : {doneCounter}')

    # Main
    def main(self, argv): 
        if len(argv) == 1 or argv[1] == 'help':
            self.help()
        elif argv[1] == 'ls':
         	self.ls()
        elif argv[1] == 'add':
            if len(argv) > 2:
                self.addTask(argv[2])
            else:
                print("Error: Missing todo string. Nothing added!")
        elif argv[1] == 'del':
        	if len(argv) > 2:
        		self.delTask(argv[2])
        	else:
        		print("Error: Missing NUMBER for deleting todo.")
        elif argv[1] == 'done':
        	if len(argv)>2:
        		self.doneTask(argv[2])
        	else:
        		print("Error: Missing NUMBER for marking todo as done.")
        elif argv[1] == 'report':
        	self.report()
        else:
            print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__":
    todo = todo()
    todo.main(sys.argv)