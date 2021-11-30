"""Module to read PDF files."""
from time import strftime
from typing import List
import subprocess
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Module to ingest strings of text from PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method for parsing PDF files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []

        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')

        tmp = f'./tmp/pdftotxt_{strftime("%Y%m%d%H%M%S")}.txt'

        subprocess.call(['pdftotext', '-layout', path, tmp])
        file_ref = open(tmp, 'r')
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0].strip().strip('"'),
                                       parsed[1].strip())
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)

        return quotes
