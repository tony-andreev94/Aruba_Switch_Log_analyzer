from log_analyzer_OOP import analyzer


class Results:

    def __init__(self):
        # analyzer.Analyzer.analyze()
        self.criticals_list = analyzer.Analyzer.found_criticals
        self.warnings_list = analyzer.Analyzer.found_warnings
        self.sysinfo_dict = analyzer.Analyzer.sysinfo
        self.log_time = list(self.sysinfo_dict.values())[0]
        self.uptime = list(self.sysinfo_dict.values())[1]
        self.sw_rev = list(self.sysinfo_dict.values())[2]
        self.pn = list(self.sysinfo_dict.values())[3]
        self.sn = list(self.sysinfo_dict.values())[4]

    def return_criticals(self):  # TODO move to formatter??
        name_string = "Critical errors found in logfile:"
        return name_string, self.criticals_list

    def return_warnings(self):
        name_string = "Warnings found in logfile:"
        return name_string, self.warnings_list

    def return_switch_info(self):
        return f"#################################\n" \
               f"USEFUL SWITCH INFORMATION:\n" \
               f"#################################\n" \
               f"Log generated on: {self.log_time}\n" \
               f"Up time: {self.uptime}\n" \
               f"Software revision: {self.sw_rev}\n" \
               f"Product number: {self.pn}\n" \
               f"Serial number: {self.sn}\n"

    def return_links(self):
        return f"#################################\n" \
               f"USEFUL LINKS:\n" \
               f"#################################\n" \
               f"Order a replacement part:\n" \
               f"http://partsurfer.hpe.com/Search.aspx?SearchText={self.pn}\n" \
               f"Download the latest software:\n" \
               f"https://h10145.www1.hpe.com/downloads/SoftwareReleases.aspx?ProductNumber={self.pn}\n"

    @staticmethod  # TODO check if static or not
    def execution_time(start_time, end_time):
        return f"Time taken: {end_time - start_time:.3f} sec."


# Testing
if __name__ == '__main__':
    # test_obj1 = Results()
    # test_obj2 = analyzer.Analyzer()
    # test_obj2.analyze()
    # print(test_obj1.criticals_list)
    # print(test_obj1.warnings_list)
    # print(test_obj1.sysinfo_dict)
    # print(list(test_obj1.sysinfo_dict.values())[3])
    # print(test_obj1.pn)
    test_obj3 = Results()
    print(test_obj3.return_criticals())
