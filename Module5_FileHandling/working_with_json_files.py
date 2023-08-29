import json

with open("F:\\data.json", "r") as file:
    data = json.loads(file.read())
    print(data)
