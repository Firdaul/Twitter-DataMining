import requests
import json


endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/DevEnvironmentAppsName.json"
# # endpoint = "https://api.twitter.com/2/tweets/search/stream/rules"

headers = {"Authorization": "Bearer INPUTYOURBEARERTOKEN",
           "Content-Type": "application/json"}

data = '{"query":"(INPUT KEYWORDS OR #HASHTAG)", "fromDate": "YYYYMMDDHHMinsMins", \
    "toDate": "YYYYMMDDHHMinsMins"}'

response = requests.post(endpoint, data=data, headers=headers).json()


with open("FILENAME.json", "w") as data:
    json.dump(response, data)