import os
import requests
import dotenv
from flask import Flask
# ------импорты------

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")
# ------константы-----
app = Flask(__name__)


@app.route('/') # главный роут
def main_route():
    return "Музыкальный усведомитель"


if __name__ == '__main__': # что будет происходить приза пуске
    app.run(port=8080, host='127.0.0.1')
