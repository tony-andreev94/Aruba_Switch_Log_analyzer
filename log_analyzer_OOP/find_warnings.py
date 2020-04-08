import re
from log_analyzer_OOP import regex


class WarningsFinder:
    """
    This class takes a line of the logfile as a string and searches for warning messages in it.
    The warning messages are represented on the whole row, so the string is returned as a result.
    """

    def __init__(self, string):
        self.string = string

    def find_warnings(self):
        if re.findall(regex.Regex.warn_regex, self.string):
            return self.string
        else:
            return None


print(WarningsFinder("W 0").find_warnings())
