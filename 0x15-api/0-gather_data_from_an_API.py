#!/usr/bin/python3

""""
A Python script that uses REST API, using a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
import sys


def get_employee_todo_process(user_id):
    """Fetch and display the TODO list progress of a given employee

    Keyword arguments:
    Args:
        user_id-- The ID of the employee
                    whose TODO list progress is to be fetched
    Return:
        None.  Prints the TODO list progress to the console.
    """

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch then user information
    user_url = f"{base_url}/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Check if user exists
    if not user_data:
        print(f"Employee with ID {user_id} not found.")
        return

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={user_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed tasks and the total number of tasks
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Print the progress
    print(
        f"Employee {user_data['name']} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
        )
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    """The main entry point of the script.  Handles command-line argument
    parsing and calls the get_employee_todo_process function.

    The script expects exactly one argument:
        1. user_id: The ID of the employee as an integer.
    """

    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Convert the command line argument to an integer (user_id)
    try:
        user_id = int(sys.argv[1])
        get_employee_todo_process(user_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
