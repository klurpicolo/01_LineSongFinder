from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a31fec076cdade512d07f44d4f58e8e8'

from LineSongFinder import routes
