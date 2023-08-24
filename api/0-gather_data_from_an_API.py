#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def get_id(id):
    """Get data from an API"""
    url = 'https://jsonplaceholder.typicode.com/'

    userResponse = requests.get(f'{url}users/{id}')
    userData = userResponse.json()
    employeeName = userData['name']

    todoResponse = requests.get(f'{url}todos?userId={id}')
    todoData = todoResponse.json()

    totalTasks = len(todoData)
    completedTasks = 0
    completedTitles = []

    for task in todoData:
        if task['completed']:
            completedTasks += 1
            completedTitles.append(task['title'])

    print(f'Employee {employeeName} is done with tasks'
          f'({completedTasks}/{totalTasks}):')

    for title in completedTitles:
        print(f'\t {title}')


if __name__ == '__main__':
    get_id(argv[1])
