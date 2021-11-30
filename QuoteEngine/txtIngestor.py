"""Module to read TXT files."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class txtIngestor(IngestorInterface):
    """Module to ingest strings of text from TXT files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method for parsing TXT files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        with open(path, 'r') as infile:
            for line in infile:
                body = line.split(' - ')[0].strip().strip('"')
                author = line.split(' - ')[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
