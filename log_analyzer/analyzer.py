import re
from log_analyzer import find_sysinfo
from log_analyzer import find_criticals
from log_analyzer import find_warnings
from log_analyzer import regex
from log_analyzer import results


class Analyzer:
    """
    03.
    Main logic, analyze the formatted logs line by line.
    Calls CriticalsFinder, WarningsFinder and SysInfoFinder classes.
    :returns self.found_criticals - list of critical errors
    :returns self.found_warnings - list with warnings
    :returns self.sysinfo - dictionary with system information
    """

    def __init__(self, formatted_logs: list):
        self.logs_formatted = formatted_logs
        self.found_criticals = []
        self.found_warnings = []
        self.sysinfo = {"Log generated on: ": "",
                        "Uptime: ": "",
                        "Software revision: ": "",
                        "Product number: ": "",
                        "Serial number: ": "",
                        }
        self.replacement_needed = False

    def analyze(self):
        for line in self.logs_formatted:
            next_index = self.logs_formatted.index(line) + 1
            if next_index < len(self.logs_formatted):
                next_line = self.logs_formatted[next_index]

            # Find warnings
            if find_warnings.WarningsFinder().find_warnings(line) is not None:
                self.found_warnings.append(line)
                if re.findall(regex.Regex.warning_multiline, next_line) is not None:
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

        return results.Results(self.sysinfo, self.found_criticals, self.found_warnings)
