import re
from log_analyzer_OOP import regex


class WarningsFinder:
    """
    This class takes a line of the logfile as a string and searches for warning messages in it.
    The warning messages are represented on the whole row, so the string is returned as a result.
    """

    # def __init__(self, string):
    #     self.string = string

    @staticmethod
    def find_warnings(string):
        if re.findall(regex.Regex.warn_regex, string):
            return string
        else:
            return None
