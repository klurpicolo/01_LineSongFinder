from flask import Flask, request, abort
from LineSongFinder import line_api
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Fuck You Papol"


@app.route("/about")
def about():
    return "<h1>Here is about page</h1>"


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


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8080)
