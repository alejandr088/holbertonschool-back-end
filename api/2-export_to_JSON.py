#!/usr/bin/python3
""" Export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    tasks = []
    for task in todo:
        tasks.append({"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": user.get("username")})

    data = {user_id: tasks}
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)
