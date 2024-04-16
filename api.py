import dotenv
import base64

import requests
from requests import post
import json
import os

dotenv.load_dotenv()
TOKEN = os.environ.get("API_TOKEM_DISCOGS")
url = f"https://api.discogs.com/database/search?q=Nirvana&token={TOKEN}"
