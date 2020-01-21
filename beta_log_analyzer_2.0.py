import os
import re
import time

start_time = time.time()

# [24;1H[2K[24;1H[1;24r[24;1H

username = os.getlogin()
# TO_DO: add filename via user input
file_path = 'C:\\Users\\'+username+'\\Documents\\@Python\\sta.txt'

# TO_DO: add more error conditions
critical_errors_list = ["Other Fault", "Fan failure", "MM1  Failed", "MM2  Failed",
                        "Unrecoverable fault on PoE controller", "PD Other Fault"]

warning = ""
second_warning = ""
warning_list = []
# test_list for warning_list testing
test_list = []
product_number = ""

errors_counter = 0
previous_line = ""
# previous_line = str --- TypeError: "argument of type 'type' is not iterable ??
# print(type(previous_line))

log_time = str
software_rev = str
up_time = str

print("#################################")
print(f"Critical errors found in logfile:")
print("#################################")
print()


with open(file_path) as file_object:
    for line in file_object:
        # Breaking out of the file so we don't check the whole file unnecessarily
        if 'Bottom of Log :' in line:
            break
        for error_element in critical_errors_list:
            if error_element in line:
                errors_counter += 1
                print(line.rstrip())
        # warning_regex = re.search(r"[W]\s\d{2}[/]\d{2}[/]\d{2}", line)

        # TO_DO: put this info at the top - append critical errors into a list or another for loop?
        #        ask user if this info is to be included?
        if 'Up Time' in line:
            up_time = line
            up_time_regex = re.search(r"\d+\s\w+", up_time)
        if 'Software revision' in line:
            software_rev = line
            software_rev_regex = re.search(r"\w{2}[.]\w+[.]\w+[.]\w+", software_rev)
        if 'show time' in previous_line:
            log_time = line
        if 'Product:   HP J' in line:
            product_number = line
            product_number_regex = re.search(r"[J]\w\d{3}\w", product_number)
        # TO_DO: add these two IFs into a single if - using or makes every line to get appended in the list
        # TO_DO: add major errors: M 03/07/18 08:48:32 02796 chassis: AM1: Internal power supply 1 inserted. Total
        if 'W 0' in previous_line:
            # Deal with 1- or 2-line warnings with doing the check in "previous_line"
            # use regex to check if "line" starts with whitespace - print it as well.
            warning = previous_line
            warning_list.append(warning)
            if re.search(r"[\s]", line):
                second_warning = line
                warning_list.append(second_warning)
            warning_list.append(warning)
        if 'W 1' in line:
            warning = line
            warning_list.append(warning)

        # previous_line used for output on the next line (show time)
        previous_line = line

if errors_counter == 0:
    print('No critical errors were found in the logfile.')
else:
    print()
    print('Possible replacement needed.')
    print()

print()
print("#################################")
print(f"USEFUL SWITCH INFORMATION: ")
print("#################################")
print()
print(f"Log generated on: {log_time.rstrip()}")
print(f"Software revision: {software_rev_regex.group()}")
print(f"Uptime: {up_time_regex.group()}")
print(f"Product number: {product_number_regex.group()}")
print()
print()


print("#################################")
print(f"USEFUL LINKS: ")
print("#################################")
print(f"http://partsurfer.hpe.com/Search.aspx?SearchText={product_number_regex.group()}")
print(f"https://h10145.www1.hpe.com/downloads/SoftwareReleases.aspx?ProductNumber={product_number_regex.group()}")
print()
print()
print("#################################")
print(f"Warnings found:")
print("#################################")
# TO_DO: remove empty line between each warning, fix issue with warnings on two lines
print(*warning_list)

print("--- %s seconds ---" % (time.time() - start_time))
#print(warning_list[:])
#print(test_list[:])
