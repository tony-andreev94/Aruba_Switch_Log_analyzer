import re
from log_analyzer_OOP import regex


class SysInfoFinder:

    def __init__(self, string):
        self.string = string  # line
        self.reg_exp = regex.Regex

    def find_time(self):
        if "show time" in self.string:
            return True

    def find_uptime(self):  # TODO change findall method with finditer
        if len(re.findall(self.reg_exp.uptime_regex, self.string)) > 0:
            return "".join(re.findall(self.reg_exp.uptime_regex, self.string))

    def find_sw_version(self):
        if len(re.findall(self.reg_exp.sw_regex, self.string)) > 0:
            return "".join(re.findall(self.reg_exp.sw_regex, self.string))

    def find_product(self):
        if len(re.findall(self.reg_exp.pn_regex, self.string)) > 0:
            return "".join(re.findall(self.reg_exp.pn_regex, self.string))

    def find_serial(self):
        if len(re.findall(self.reg_exp.sn_regex, self.string)) > 0:
            return "".join(re.findall(self.reg_exp.sn_regex, self.string))
