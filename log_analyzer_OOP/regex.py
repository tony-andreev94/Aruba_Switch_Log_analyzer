class Regex:
    uptime_regex = r"(?<=Up Time\s{12}:\s)\d{2}\s\w+"
    sn_regex = r"(?<=Serial Number\s{6}:\s)\w{10}"
    sw_regex = r"(?<=Software revision\s{2}:\s)\w+.\d+.\d+\.?\d+"
    pn_regex = r"(?<=Product:\s{3}HP\s)\w{6}"
    warn_regex = r"[W|M]\s\d"
    warn_regex_2 = r"^\s{2}"  # regex to catch the second line of multiline warning messages
