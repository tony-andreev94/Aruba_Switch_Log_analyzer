import re
from log_analyzer import regex


class WarningsFinder:
    """
    This class takes a line of the logfile as a string and searches for warning messages in it.
    The warning messages take up a whole line in the logfile, therefore the  input string is returned as a result if the regex is matched.
    :returns 'string'
    """

    @staticmethod
    def find_warnings(string):
        if re.findall(regex.Regex.warning, string):
            return string
        else:
            return None
