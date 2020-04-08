class CriticalsFinder:
    """
    This class takes a line of the logfile as a string and searches for critical errors in it.
    The critical errors are represented on the whole row, so the string is returned as a result.
    """
    critical_errors_list = ["Other Fault", "Fan failure", "MM1  Failed", "MM2  Failed", "Faulted", "PD Other Fault",
                            "Unrecoverable fault on PoE controller", "Failures", "selftest failure"]

    def __init__(self, string):
        self.string = string

    def find_criticals(self):
        for each in self.critical_errors_list:
            if each in self.string:
                return each
            else:
                return None
