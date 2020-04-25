class CriticalsFinder:
    """
    This class takes a line of the logfile as a string and searches for critical errors in it.
    The critical errors are represented on the whole row, so the string is returned as a result.
    """
    CRITICAL_ERRORS_LIST = ["Other Fault", "Fan failure", "MM1  Failed", "MM2  Failed", "Faulted", "PD Other Fault",
                            "Unrecoverable fault on PoE controller", "Failures", "selftest failure"]

    @staticmethod
    def find_criticals(string):
        for each in CriticalsFinder.CRITICAL_ERRORS_LIST:
            if each in string:
                return string

# Testing
# test_obj = CriticalsFinder('Unrecoverable fault on PoE controller')
# test_obj2 = CriticalsFinder('PD Other Fault')
# print(test_obj.find_criticals())
# print(test_obj2.find_criticals())
