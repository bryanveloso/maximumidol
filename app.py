import os
import requests

from flash import Flask, request, render_template


IDOL_SOURCE = 'http://aidoru-bomb.herokuapp.com/random'


@app.route('/')
def home():
    r = requests.get(IDOL_SOURCE)
    gif = r.json.get('idol', '')
    return render_template('', gif=gif)


@app.route('/random')
def random_gif():
    r = requests.get(IDOL_SOURCE)
    return r.json


if __name__ = '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
