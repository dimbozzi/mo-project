def add_task():
  task = input("enter your tasks : ")
  tasks.append(task)
  print(task + " added to the list ")



def mark_task_complete():
  task_number = int(input("enter the number of the task you want to mark as complete : "))
  tasks[task_number - 1] = "[x] " + tasks[task_number - 1]

def view_tasks():
  for i in range(len(tasks)):
    print(i+1 ,tasks[i])


message = """1 - Add tasks to the list 
2 - mark as complete
3 - view tasks 
4 - quit """

tasks =[]

while True:
  print(message)
  choice = input("enter your choice :  ")

  if choice == "1":
    add_task()
  elif choice == "2":
    mark_task_complete()
  elif choice == "3":
    view_tasks()
  elif choice == "4":
    break
  else:
    
    print("invalid choice  : please enter a num from 1 to 4 ")



