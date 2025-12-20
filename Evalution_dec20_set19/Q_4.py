import requests
from datetime import datetime

api_url = "https://reqres.in/api/users"
headers = {
    "Authorization": "Bearer reqres-token",
    "Content-Type": "application/json"
}
payload = {
    "name": "neo",
    "job": "chosen"
}


response = requests.post(api_url, headers=headers, json=payload)


data = response.json()


created_at_str = data.get("createdAt")


date_obj = datetime.strptime(created_at_str[:10], "%Y-%m-%d")
result_year = date_obj.year


print(result_year)