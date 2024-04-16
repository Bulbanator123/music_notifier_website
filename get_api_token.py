import dotenv
import base64

import requests
from requests import post
import json
import os

dotenv.load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID_SPOTIFY")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET_SPOTIFY")


def get_api_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    response = requests.get(query_url, headers=headers)
    json_result = json.loads(response.content)["artists"]["items"]

    if len(json_result) == 0:
        print("Нет такого артиста")
        return None

    return json_result[0]


def get_songs_by_the_artist(token, artist_name):
    url = f"https://api.spotify.com/v1/search?type=track&q=artist:{artist_name}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    json_result = json.loads(response.content)
    print(json_result["tracks"])


token = get_api_token()
get_songs_by_the_artist(token, search_artist(token, "E-type")["name"])
