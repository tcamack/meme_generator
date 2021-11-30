"""Module to read DOCX files."""
from docx import Document
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Module to ingest strings of text from DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method for parsing DOCX files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
