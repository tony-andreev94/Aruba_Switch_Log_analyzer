import os
from log_analyzer_OOP import file_handler


class FileLoader:
    """
    01.
    In this class the logfile is loaded, each line is read and appended to a list and passed to the 'FileHandler' class.
    :returns self.logs
    """

    def __init__(self):
        # windows path:
        self.username = os.getlogin()
        self.path = 'C:\\Users\\' + self.username + '\\Documents\\@Python\\sta.txt'  # TODO alternative path/input
        # linux path:
        # self.path = '/media/tony/DATA/Documents/@Python/sta.txt'
        self.logs = []
        self.formatted_logs = []

    def load_file(self):
        with open(self.path) as file_object:
            # basic error handling:
            # check file extention .log . txt
            for line in file_object:
                self.logs.append(line)
            # we have the loaded file

        return self.logs


# Testing purpose
if __name__ == '__main__':
    test_obj = FileLoader()
    print(test_obj.load_file())
    # print(result.__doc__)
