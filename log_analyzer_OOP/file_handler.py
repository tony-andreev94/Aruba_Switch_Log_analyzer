import re
from log_analyzer_OOP import file_loader


class FileHandler:
    """
    02.
    This class takes the list of log messages removes all empty lines, strips extra whitespaces and stops if
    'Bottom of Log :' is reached, as no other meaningful information is analyzed after this line at this point.
    (1300 lines checked instead of 20000 etc.)

    :returns self.logs_formatted
    """

    def __init__(self):
        file_object = file_loader.FileLoader()  # TODO better name (file_object)
        self.logs_list = file_object.load_file()  # TODO not sure
        # self.logs_list = file_loader.FileLoader.load_file() missing positional argument: self
        self.logs_formatted = []  # make private? there is a shadow in analyzer

    def format_logs(self):
        for line in self.logs_list:
            if 'Bottom of Log :' in line:
                break
            if re.match(r'^\s*$', line) is None:  # removes empty lines #TODO make the regex a variable in regex.py
                self.logs_formatted.append(line.strip())
        return self.logs_formatted


# Testing purpose
if __name__ == '__main__':
    test_obj = FileHandler()
    print(test_obj.format_logs())
