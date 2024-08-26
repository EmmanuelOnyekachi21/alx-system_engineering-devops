#!/usr/bin/python3

""""
export the employee's tasks to a CSV file
"""

import json
import requests
import sys


def export_to_json(user_id):
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

    file_name = f"{user_id}.json"

    tasks = [
        {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_data['username']
        }

        for todo in todos_data
    ]

    # Dictionary to store the employee's tasks
    employee_tasks = {str(user_id): tasks}

    with open(file_name, 'w') as file:
        json.dump(employee_tasks, file)

    print(f"Data exported to {file_name}")


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
        export_to_json(user_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
