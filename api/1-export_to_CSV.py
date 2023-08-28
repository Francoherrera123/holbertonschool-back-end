#!/usr/bin/python3
"""
    This a Python script thatfor a given employee ID, returns information about
        his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import sys
    from urllib import request
    import csv

    empId = sys.argv[1]

    url = request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(empId))

    info = json.loads(url.read().decode("utf-8"))

    url_task = request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(empId))
    tasks = json.loads(url_task.read().decode("utf-8"))

    csv.register_dialect("Dialect", quoting=csv.QUOTE_ALL)
    with open(f"{empId}.csv", "w+") as file:
        csvwriter = csv.writer(file, dialect="Dialect")
        for row in tasks:
            csvwriter.writerow([row['userId'], info["username"],
                                row["completed"], row["title"]])