#!/usr/bin/python3
""" Export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        user_id = user.get("id")
        todo = requests.get(url + "todos", params={"userId": user_id}).json()
        tasks = []
        for task in todo:
            tasks.append({"username": user.get("username"),
                          "task": task.get("title"),
                          "completed": task.get("completed")
                          })
        data[user_id] = tasks
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
