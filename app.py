import os
import requests

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.debug = True

# Hard-coded source of IDOLS.
IDOL_SOURCE = 'http://aidoru-bomb.herokuapp.com/random'


@app.route('/')
@app.route('/random')
def home():
    r = requests.get(IDOL_SOURCE)
    gif = r.json.get('idol', '')
    return render_template('home.html', gif=gif)


@app.route('/fetch')
def fetch_gif():
    r = requests.get(IDOL_SOURCE)
    return jsonify(r.json)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
