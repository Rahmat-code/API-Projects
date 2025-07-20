import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

USERNAME = "rahmathussain"
TOKEN = os.getenv("TOKEN")

create_user_url = "https://pixe.la/v1/users"

create_user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=create_user_url, json=create_user_body)

#print(response.text)

create_graph_url = f"{create_user_url}/{USERNAME}/graphs"

create_graph_body = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Kolkata"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=create_graph_url, json=create_graph_body, headers=headers)

#print(response.text)

post_pixel_url = f"{create_graph_url}/{create_graph_body['id']}"
current_date = datetime.now().strftime("%Y%m%d")
post_pixel_body = {
    "date": "20250719",
    "quantity": "5.5"
}

#response = requests.post(url=post_pixel_url, json=post_pixel_body, headers=headers)

#print(response.text)

put_pixel_url = f"{post_pixel_url}/{current_date}"
put_pixel_body = {
    "quantity": "4.0"
}

response = requests.put(url=put_pixel_url, json=put_pixel_body, headers=headers)

print(response.text)