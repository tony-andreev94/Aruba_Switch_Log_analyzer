class Results:
    """
    04.
    This class takes 3 arguments passed by the analyze() method of the Analyzer class.
    These arguments contain the useful information after the analysis is done.
    This information is formatted and printed using the print_results() method.
    """

    def __init__(self, sysinfo: dict, critical_errors: list, warning_messages: list):
        self.sysinfo_dict = sysinfo
        self.criticals_list = critical_errors
        self.warnings_list = warning_messages
        self.formatted_results = []

    def print_switch_info(self):
        print("#################################\nUSEFUL SWITCH INFORMATION: \n#################################\n")
        for key, value in self.sysinfo_dict.items():
            print(key, value)
        print("\n")

    def print_links(self):
        pn = self.sysinfo_dict['Product number: ']
        print("#################################\nUSEFUL LINKS: \n#################################\n")
        print("Order a replacement part:")
        print(f"http://partsurfer.hpe.com/Search.aspx?SearchText={pn}")
        print("Download the latest software:")
        print(f"https://h10145.www1.hpe.com/downloads/SoftwareReleases.aspx?ProductNumber={pn}")
        print("\n")

    def print_criticals(self):
        print("#################################\nCRITICAL ERRORS FOUND: \n#################################\n")
        if self.is_not_empty(self.criticals_list):
            for each_error in self.criticals_list:
                print(each_error)
            print("Consider part replacement.\n\n")
        else:
            print("No critical error messages were found in the logfile.\n\n")

    def print_warnings(self):
        print("#################################\nWARNING MESSAGES FOUND: \n#################################\n")
        if self.is_not_empty(self.warnings_list):
            for each_warning in self.warnings_list:
                print(each_warning)
            print("\n\n")
        else:
            print("No critical error messages were found in the logfile.\n\n")

    def print_results(self):
        self.print_switch_info()
        self.print_links()
        self.print_criticals()
        self.print_warnings()

    @staticmethod
    def is_not_empty(input_list):
        if len(input_list) > 0:
            return True
        return False
