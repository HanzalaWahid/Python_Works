import json

with open("amd.json")  as file:
    req = json.load(file)
    # print(type(json.loads(file)))

print(type(req))

import json

with open("amd.json") as f:
    q = json.load(f)

# print(q)
print(q["maxAge"])
