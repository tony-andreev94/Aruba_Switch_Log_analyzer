import re
from log_analyzer_OOP import file_handler
from log_analyzer_OOP import find_sysinfo
from log_analyzer_OOP import find_criticals
from log_analyzer_OOP import find_warnings
from log_analyzer_OOP import regex


class Analyzer:
    """
    03.
    Main logic, analyze the formatted logs line by line.
    Calls CriticalsFinder, WarningsFinder and SysInfoFinder classes.
    :returns self.found_criticals - list of critical errors
    :returns self.found_warnings - list with warnings
    :returns self.sysinfo - dictionary with system information
    """

    def __init__(self):
        log_file = file_handler.FileHandler()
        self.logs_formatted = log_file.format_logs()  # tuk e input loga - <class 'list'>
        self.found_criticals = []
        self.found_warnings = []
        self.sysinfo = {"Log generated on: ": "",
                        "Uptime: ": "",
                        "Software revision: ": "",
                        "Product number: ": "",
                        "Serial number: ": "",
                        }

    def analyze(self):
        # error check - check if "show tech all" is in the file
        for line in self.logs_formatted:
            next_index = self.logs_formatted.index(line) + 1
            if next_index < len(self.logs_formatted):
                next_line = self.logs_formatted[next_index]

            # Find warnings
            if find_warnings.WarningsFinder().find_warnings(line) is not None:
                self.found_warnings.append(line)
                if re.findall(regex.Regex.warn_regex_2, next_line) is not None:
                    self.found_warnings.append(next_line)

            # Find criticals
            if find_criticals.CriticalsFinder().find_criticals(line) is not None:
                self.found_criticals.append(line)

            # Find Up Time:
            if find_sysinfo.SysInfoFinder().find_uptime(line) is not None:
                up_time = find_sysinfo.SysInfoFinder().find_uptime(line)
                self.sysinfo["Uptime: "] = up_time

            # Find Time (log generated on:)
            if find_sysinfo.SysInfoFinder().find_time(line) is True:
                self.sysinfo["Log generated on: "] = next_line

            # Find Software Version:
            if find_sysinfo.SysInfoFinder().find_sw_version(line) is not None:
                sw_rev = find_sysinfo.SysInfoFinder().find_sw_version(line)
                self.sysinfo["Software revision: "] = sw_rev

            # Find Product Number:
            if find_sysinfo.SysInfoFinder().find_product(line) is not None:
                pn = find_sysinfo.SysInfoFinder().find_product(line)
                self.sysinfo["Product number: "] = pn

            # Find Serial Number:
            if find_sysinfo.SysInfoFinder().find_serial(line) is not None:
                sn = find_sysinfo.SysInfoFinder().find_serial(line)
                self.sysinfo["Serial number: "] = sn
        #TODO add return Result(warn_list, crit_list, sysinfo_dict)


# Testing purpose
if __name__ == '__main__':
    test_obj1 = Analyzer()
    test_obj1.analyze()
    print(f"Found criticals:")
    print(test_obj1.found_criticals)
    print("\nFound warnings:")
    print(test_obj1.found_warnings)
    print("\nSystem info:")
    print(test_obj1.sysinfo)
