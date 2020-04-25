import re
from log_analyzer_OOP import regex


class SysInfoFinder:
    reg_exp = regex.Regex

    @staticmethod
    def find_time(string):
        if "show time" in string:
            return True

    @staticmethod
    def find_uptime(string):  # TODO change findall method with finditer
        if len(re.findall(regex.Regex.uptime_regex, string)) > 0:
            return "".join(re.findall(regex.Regex.uptime_regex, string))

    @staticmethod
    def find_sw_version(string):
        if len(re.findall(regex.Regex.sw_regex, string)) > 0:
            return "".join(re.findall(regex.Regex.sw_regex, string))

    @staticmethod
    def find_product(string):
        if len(re.findall(regex.Regex.pn_regex, string)) > 0:
            return "".join(re.findall(regex.Regex.pn_regex, string))

    @staticmethod
    def find_serial(string):
        if len(re.findall(regex.Regex.sn_regex, string)) > 0:
            return "".join(re.findall(regex.Regex.sn_regex, string))
