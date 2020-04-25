import re
from log_analyzer import regex


class FileHandler:
    """
    02.
    This class takes the list of log messages removes all empty lines, strips extra whitespaces and stops if
    'Bottom of Log :' is reached, as no other meaningful information is analyzed after this line at this point.
    (1300 lines checked instead of 20000 etc.)

    :returns self.logs_formatted
    """

    def __init__(self, input_list):
        self.logs_list = input_list
        self.logs_formatted = []

    def format_logs(self):
        for line in self.logs_list:
            if 'Bottom of Log :' in line:
                break
            if re.match(regex.Regex.empty_line, line) is None:
                self.logs_formatted.append(line.strip())
        return self.logs_formatted
