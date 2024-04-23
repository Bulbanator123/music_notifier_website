import os
import requests
import dotenv
import datetime
import random
from flask import Flask, render_template, make_response, jsonify
from flask_login import LoginManager, login_required
from data import db_session
from data.users import User
from data.favours import Favours
from forms.user import RegisterForm, LoginForm

# ------импорты------

dotenv.load_dotenv()

TOKEN = os.environ.get("API_TOKEM_DISCOGS")
SECRET_KEY = os.environ.get("SECRET_KEY")
# ------ENV---------
# ----константы-----

app = Flask(__name__)  # создание приложения
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/artist')  # роут артиста
def artist_route():
    params = {"title": "Артист"}
    return render_template("artist.html", **params)


@app.route('/artist/music')  # роут музыки
def music_route():
    params = {"title": "Музыка"}
    return render_template("music.html", **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


async def update_API():  # обновление данных из api
    pass


def main():  # отдельно-вынесенная функция main
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':  # что будет происходить при запуске
    main()
