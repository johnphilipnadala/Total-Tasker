import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def to_do_list_program():
    tasks = load_tasks()

    print("Welcome to the Total Tasker: Your Partner for Prioritizing Productivity")

    while True:
        print("\nMenu: Choose a number to perform an action")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Remove Tasks")
        print("0. Exit Total Tracker")
        choice = input("\nChoose an option: ")

        if choice == "0":
            print("\nThank you for using Total Tasker. Goodbye!")
            break

        elif choice == "1":
            task_name = input("\nEnter the task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            priority = input("Enter the priority (High, Medium, Low): ")

            if task_name and due_date and priority:
                tasks[task_name] = {
                    "due_date": due_date,
                    "priority": priority
                }
                save_tasks(tasks)
                print(f"\nTask '{task_name}' added successfully!")
            else:
                print("\nError: All fields are required to add a task.")

        elif choice == "2":
            if tasks:
                print("\nYour Tasks:")
                for task_name, details in tasks.items():
                    print(f"- {task_name} (Due: {details['due_date']}, Priority: {details['priority']})")
            else:
                print("\nNo tasks found.")

        elif choice == "3":
            task_name = input("\nEnter the task name to remove: ")
            if task_name in tasks:
                del tasks[task_name]
                save_tasks(tasks)
                print(f"\nTask '{task_name}' removed successfully!")
            else:
                print(f"\nError: Task '{task_name}' not found.")

        else:
            print("\nInvalid choice. Please try again.")

to_do_list_program()