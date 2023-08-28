#!/usr/bin/python3
"""
    This a Python script thatfor a given employee ID, returns information about
        his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request
    import json

    dict_user = {}
    url = request.urlopen(
        "https://jsonplaceholder.typicode.com/users/")

    info = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos")
    tasks = json.loads(url_task.read().decode("utf-8"))

    for user in info:
        user_id = str(user["id"])
        user_tasks = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in tasks if task["userId"] == user["id"]
        ]
        dict_user[user_id] = user_tasks
    with open(f"todo_all_employees.json", "w+") as file:
        file.write(json.dumps(dict_user))
        file.close()