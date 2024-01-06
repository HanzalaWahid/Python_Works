

import requests
import json

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"

req = requests.get(url).text
# print(req)

data = json.loads(req)
print(data)
