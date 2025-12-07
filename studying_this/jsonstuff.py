import json as json


file = open("../decisions.json")
jsonString = file.read()
file.close()

jsonObject = json.loads(jsonString)
print(jsonObject["discard"])

file =