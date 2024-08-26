#!/usr/bin/python3

""""
Script to fetch to-do tasks from an API, organize them by user ID,
and save them in a JSON file.

The script fetches to-do tasks for all users from the JSONPlaceholder API
and structures the data by user ID. Each user ID maps to a list of tasks,
where each task includes the username, task title, and completion status.
The output is saved in a JSON file named `todo_all_employees.json`.

Usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests
import sys


def fetch_data():
    """Fetch to-do tasks for all users from the JSONPlaceholder API.

    Returns:
        dict: A dictionary where the keys are user IDs,
        and the values are lists of tasks.
    """

    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def process_data(users, todos):
    """Process the data.
    """
    # Create a dictionary to hold the results
    result = {}

    # Map user ids to username
    user_id_to_username = {user['id']: user['username'] for user in users}

    for todo in todos:
        user_id = str(todo['userId'])
        username = user_id_to_username.get(todo['userId'])

        if user_id not in result:
            result[user_id] = []

        result[user_id].append({
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        })

    return result


def save_to_file(data):
    """ Save the dictionary to a JSON file"""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file, indent=4)


def main():
    """main"""
    users, todos = fetch_data()
    data = process_data(users, todos)
    save_to_file(data)


if __name__ == "__main__":
    main()
