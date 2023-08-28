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

    empId = sys.argv[1]

    url = request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(empId))

    info = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empId))
    tasks = json.loads(url_task.read().decode("utf-8"))

    index = "{}".format(info["id"])
    dict_user = {
        index: []
    }
    for task in tasks:
        dict_user[index].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": info["username"]
        })

    with open(f"{empId}.json", "w+") as file:
        file.write(json.dumps(dict_user))
        file.close()