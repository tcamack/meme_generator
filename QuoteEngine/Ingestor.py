"""Module that contains class to select ingestor module."""
from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .txtIngestor import txtIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Class to select ingestor module."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, txtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse paths for correct ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
