import os
import requests

from flask import Flask, jsonify, render_template
from flask_s3 import FlaskS3

# Hard-coded source of IDOLS.
IDOL_SOURCE = 'http://aidoru-bomb.herokuapp.com/random'

# Let's create a Flask.
app = Flask(__name__)
app.debug = getattr(os.environ, 'DEBUG', False)

# FlaskS3 Configuration
app.config['S3_BUCKET_NAME'] = 'maximumidol'
app.config['S3_USE_HTTPS'] = 'false'
s3 = FlaskS3(app)


@app.route('/')
@app.route('/random')
def home():
    r = requests.get(IDOL_SOURCE)
    gif = r.json.get('idol', '')
    return render_template('home.html', gif=gif)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/fetch')
def fetch_gif():
    r = requests.get(IDOL_SOURCE)
    return jsonify(r.json)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
