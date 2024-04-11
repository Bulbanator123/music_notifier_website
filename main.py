import os
import requests
import dotenv
from flask import Flask, render_template
from data import db_session

# ------импорты------

dotenv.load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
# ------ENV---------
# ----константы-----

app = Flask(__name__)  # создание приложения
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')  # главный роут
def main_route():
    params = {"title": "Music Notifier"}
    return render_template("main.html", **params)


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
