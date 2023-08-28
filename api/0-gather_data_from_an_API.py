#!/usr/bin/python3
"""
    This a Python script that for a given employee ID
      returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    import sys

    empId = sys.argv[1]

    info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(empId)).json()

    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(empId)).json()

    completed = list(filter(lambda task: task["completed"], tasks))

    print("Employee {} is done with tasks({}/{}):".
          format(info["name"], len(completed), len(tasks)))
    title = [task["title"] for task in completed]
    for text in title:
        print("\t {}".format(text))