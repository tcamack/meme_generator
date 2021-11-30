"""Module for running Flask web interface."""
from flask import Flask, render_template, request
import os
import random
import requests

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

static_dir = './static'
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

meme = MemeEngine(static_dir)


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for quote_file in quote_files:
        print(quote_file)
        quotes += Ingestor.parse(quote_file)
        print(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith('.jpg'):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form['image_url']:
        return render_template('meme_form.html')

    image_url = request.form['image_url']

    try:
        r = requests.get(image_url)
        r.raise_for_status()
        tmp = f'./tmp/{random.randint(0, 1000000)}.png'
        img = open(tmp, 'wb').write(r.content)

    except requests.exceptions.HTTPError as error:
        print(error)
        return render_template('meme_form.html')

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
