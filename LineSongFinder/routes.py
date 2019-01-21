from flask import request, abort, render_template, url_for
import json
from LineSongFinder import app
from LineSongFinder import line_api, model


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='home')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/history")
def history():
    line_db_util = model.db_util()
    records = line_db_util.retrieve_data()
    return render_template('history.html', records=records)


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
