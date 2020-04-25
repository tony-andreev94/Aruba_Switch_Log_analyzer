import re
from log_analyzer import regex


class SysInfoFinder:
    """
    This class takes a string as an input and checks if it contains system related information.
    :returns the matched regex object as a string
    """
    reg_exp = regex.Regex

    @staticmethod
    def find_time(string):
        if "show time" in string:
            return True

    @staticmethod
    def find_uptime(string):
        if len(re.findall(regex.Regex.uptime, string)) > 0:
            return "".join(re.findall(regex.Regex.uptime, string))

    @staticmethod
    def find_sw_version(string):
        if len(re.findall(regex.Regex.sw, string)) > 0:
            return "".join(re.findall(regex.Regex.sw, string))

    @staticmethod
    def find_product(string):
        if len(re.findall(regex.Regex.pn, string)) > 0:
            return "".join(re.findall(regex.Regex.pn, string))

    @staticmethod
    def find_serial(string):
        if len(re.findall(regex.Regex.sn, string)) > 0:
            return "".join(re.findall(regex.Regex.sn, string))
