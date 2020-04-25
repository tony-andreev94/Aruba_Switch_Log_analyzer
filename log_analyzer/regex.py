class Regex:
    """
    This class contains all regular expressions used in the project.
    """
    empty_line = r"^\s*$"
    uptime = r"(?<=Up Time\s{12}:\s)\d+\s\w+"
    sn = r"(?<=Serial Number\s{6}:\s)\w{10}"
    sw = r"(?<=Software revision\s{2}:\s)\w+.\d+.\d+\.?\d+"
    pn = r"(?<=Product:\s{3}HP\s)\w{6}"
    warning = r"[W|M]\s\d"
    warning_multiline = r"^\s{2}"  # regex to catch the second line of multiline warning messages
