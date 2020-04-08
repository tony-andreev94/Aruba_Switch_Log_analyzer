import os


class FileLoader:
    """
    01.
    In this class the logfile is loaded, each line is read and appended to a list and passed to the 'FileHandler' class.
    :returns self.logs
    """
    def __init__(self):
        self.username = os.getlogin()
        self.path = 'C:\\Users\\' + self.username + '\\Documents\\@Python\\sta.txt'  # TODO alternative path/input
        self.logs = []

    def load_file(self):
        # load file and remove whitespace
        with open(self.path) as file_object:
            for line in file_object:
                self.logs.append(line)
        return self.logs


# Testing purpose
if __name__ == '__main__':
    result = FileLoader()
    print(result.load_file())
