"""Module to read CSV files."""
from pandas import read_csv
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Module to ingest strings of text from CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method for parsing PDF files."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quotes = []

        file = read_csv(path, header=0)

        for index, row in file.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
