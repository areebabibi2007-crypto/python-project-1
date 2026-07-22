# file_handler.py

import os
from task_manager import tasks

filename = "tasks.txt"


def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks.clear()
            for line in file:
                tasks.append(line.strip())


def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")