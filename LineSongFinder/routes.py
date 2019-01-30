from flask import request, abort, render_template, url_for, flash, redirect
import json
from LineSongFinder import app, line_api, model, song_recog_api
from LineSongFinder.forms import RegistrationForm, LoginForm, SearchForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        queries = [{'artist_name': 'BodySlam',
                    'track_name': 'Love',
                    'lyric': 'This love is taken to hard on me. You say goodbye.~'},
                   {'artist_name': 'P-Bird',
                    'track_name': 'qwertyyuiuy',
                    'lyric': 'I found a love for me Darling just dive right in'}]
        print(form.query_text.data)
        queries = song_recog_api.get_search_list_musixmatch_web(form.query_text.data)
        return render_template('search.html', title='Search', form=form, queries=queries)
    return render_template('search.html', title='Search', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/history")
def history():
    line_db_util = model.db_util()
    records = reversed(line_db_util.retrieve_data())
    return render_template('history.html', title='History', records=records)


# @app.route("/test")
# def test():
#     line_db_util = model.db_util()
#     records = line_db_util.retrieve_data()
#     return render_template('test.html', title='test', records=records)


@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Print pretty Json
        request_str = json.dumps(request.json, indent=4)
        print(request_str)

        line_api.reply_guess_song(request)

        return '', 200
    else:
        about(400)
