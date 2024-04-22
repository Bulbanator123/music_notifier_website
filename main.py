import os
import requests
import dotenv
import datetime
import random
from flask import Flask, render_template, make_response, jsonify
from data import db_session

# ------импорты------

dotenv.load_dotenv()

TOKEN = os.environ.get("API_TOKEM_DISCOGS")
SECRET_KEY = os.environ.get("SECRET_KEY")
# ------ENV---------
# ----константы-----

app = Flask(__name__)  # создание приложения
app.config['SECRET_KEY'] = SECRET_KEY


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/')  # главный роут
def main_route():
    url1 = f"https://api.discogs.com/database/search?q=&type=release&format=MP3&year={datetime.datetime.now().year}&page={random.randint(1, 972)}&per_page=10&token={TOKEN}"
    response1 = requests.get(url1).json()
    url2 = f"https://api.discogs.com/database/search?q=&type=release&format=album&year={datetime.datetime.now().year}&page={random.randint(1, 1000)}&per_page=10&token={TOKEN}"
    response2 = requests.get(url2).json()
    params = {"title": "Music Notifier", "music": [[el["title"], el["cover_image"]] for el in response1["results"]],
              "album": [[el["title"], el["cover_image"]] for el in response2["results"]]}
    return render_template("index_music.html", **params)


@app.route('/user')  # роут пользователя
def user_route():
    params = {"title": "Профиль"}
    return render_template("login.html", **params)


@app.route('/artist')  # роут артиста
def artist_route():
    params = {"title": "Артист"}
    return render_template("artist.html", **params)


@app.route('/artist/music')  # роут музыки
def music_route():
    params = {"title": "Музыка"}
    return render_template("music.html", **params)


async def update_API():  # обновление данных из api
    pass


def main():  # отдельно-вынесенная функция main
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':  # что будет происходить при запуске
    main()
