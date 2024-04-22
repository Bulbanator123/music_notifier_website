import random

import requests
import dotenv
import datetime
import os

dotenv.load_dotenv()
TOKEN = os.environ.get("API_TOKEM_DISCOGS")
# url = f"https://api.discogs.com/database/search?q=&type=release&format=MP3&year={datetime.datetime.now().year}&page={random.randint(1, 1000)}&per_page=10&token={TOKEN}"
# print(url)
# response = requests.get(url).json()
# for el in response["results"]:
#     print(el["title"])
url1 = f"https://api.discogs.com/database/search?q=&type=release&format=MP3&year={datetime.datetime.now().year}&page={random.randint(1, 972)}&per_page=10&token={TOKEN}"
response1 = requests.get(url1).json()
url2 = f"https://api.discogs.com/database/search?q=&type=release&format=album&year={datetime.datetime.now().year}&page={random.randint(1, 972)}&per_page=10&token={TOKEN}"
response2 = requests.get(url2).json()
params = {"title": "Music Notifier", "music": [el["title"] for el in response1["results"]],
          "album": [el["title"] for el in response2["results"]]}
print(params)