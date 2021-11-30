"""Module for command line interface."""
import argparse
import os
import random

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None
    static_dir = './static'

    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine(static_dir)
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Meme Generator')
    parser.add_argument('--body',
                        type=str,
                        default=None,
                        help='Quote to appear on the picture.')
    parser.add_argument('--author',
                        type=str,
                        default=None,
                        help='Author of the quote.')
    parser.add_argument('--path',
                        type=str,
                        default=None,
                        help='File path for the background image.')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
