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

    found_criticals = []
    found_warnings = []
    sysinfo = {"Log generated on: ": "",
               "Uptime: ": "",
               "Software revision: ": "",
               "Product number: ": "",
               "Serial number: ": "",
               }

    def __init__(self):
        log_file = file_handler.FileHandler()
        self.logs_formatted = log_file.format_logs()  # tuk e input loga - <class 'list'>

    def analyze(self):
        for line in self.logs_formatted:
            next_index = self.logs_formatted.index(line) + 1
            if next_index < len(self.logs_formatted):
                next_line = self.logs_formatted[next_index]

            # Find warnings
            if find_warnings.WarningsFinder(line).find_warnings() is not None:
                self.found_warnings.append(line)
                if re.findall(regex.Regex.warn_regex_2, next_line) is not None:
                    self.found_warnings.append(next_line)

            # Find criticals
            if find_criticals.CriticalsFinder(line).find_criticals() is not None:
                self.found_criticals.append(line)

            # Find Up Time:
            if find_sysinfo.SysInfoFinder(line).find_uptime() is not None:
                up_time = find_sysinfo.SysInfoFinder(line).find_uptime()
                self.sysinfo["Uptime: "] = up_time

            # Find Time (log generated on:)
            if find_sysinfo.SysInfoFinder(line).find_time() is True:
                self.sysinfo["Log generated on: "] = next_line

            # Find Software Version:
            if find_sysinfo.SysInfoFinder(line).find_sw_version() is not None:
                sw_rev = find_sysinfo.SysInfoFinder(line).find_sw_version()
                self.sysinfo["Software revision: "] = sw_rev

            # Find Product Number:
            if find_sysinfo.SysInfoFinder(line).find_product() is not None:
                pn = find_sysinfo.SysInfoFinder(line).find_product()
                self.sysinfo["Product number: "] = pn

            # Find Serial Number:
            if find_sysinfo.SysInfoFinder(line).find_serial() is not None:
                sn = find_sysinfo.SysInfoFinder(line).find_serial()
                self.sysinfo["Serial number: "] = sn
        # return f"Criticals found:\n" \
        #        f"{self.found_criticals}\n" \
        #        f"Warnings found:\n" \
        #        f"{self.found_warnings}\n" \
        #        f"Sysinfo:\n" \
        #        f"{self.sysinfo}"
        # return self.found_criticals, self.found_warnings, self.sysinfo


# Testing purpose
if __name__ == '__main__':
    test_obj1 = Analyzer()
    test_obj1.analyze()
    print(test_obj1.found_criticals)
    print(test_obj1.found_warnings)
    print(test_obj1.sysinfo)
