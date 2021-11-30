"""Module for QuoteModel Class."""


class QuoteModel:
    """Representative model for quotes."""

    def __init__(self, body, author):
        """
        Create new QuoteModel.

        :param body: content of quote
        :param author: author of quote
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return string representation of QuoteModel (body - author)."""
        return f'{self.body} - {self.author}'
