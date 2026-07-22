# task_manager.py

tasks = []


def add_task(task):
    tasks.append("[ ] " + task)
    print("task added successfully")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def update_task(index, new_task):
    if 0 <= index < len(tasks):
        if tasks[index].startswith("[X]"):
            tasks[index] = "[X] " + new_task
        else:
            tasks[index] = "[ ] " + new_task
        print("Task Updated Successfully!")
    else:
        print("Invalid Task Number!")


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task Deleted Successfully!")
    else:
        print("Invalid Task Number!")


def complete_task(index):
    if 0 <= index < len(tasks):
        if tasks[index].startswith("[ ]"):
            tasks[index] = tasks[index].replace("[ ]", "[X]", 1)
            print("Task Completed!")
        else:
            print("Task Already Completed.")
    else:
        print("Invalid Task Number!")