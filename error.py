__author__ = "wmyers559"

class Error(Exception):
    """Base error class that all the others are derived from."""

    pass


class KeywordError(Error):
    """Exception to be raised whenever someone tries to interact with an object in an forbidden way."""

    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
       return "Unknown keyword \"" + self.keyword + "\"."
