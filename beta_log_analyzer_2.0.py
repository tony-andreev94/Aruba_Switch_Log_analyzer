# TODO: Add a general description of the program? Good Practices?!
import os
import re
import time

start_time = time.time()
# Setting up a variable that gets the user's username
username = os.getlogin()
# TODO: add filename or file path via user input?
file_path = 'C:\\Users\\' + username + '\\Documents\\@Python\\sta.txt'

# A list with critical error messages to be searched in the logs
critical_errors_list = ["Other Fault", "Fan failure", "MM1  Failed", "MM2  Failed", "Faulted", "PD Other Fault",
                        "Unrecoverable fault on PoE controller", "Failures", "selftest failure"]

warning = ""  # variable to store found warning
second_warning = ""  # used to catch two line warnings
warnings_found = []  # stores warnings
criticals_found = []  # stores critical errors
product_n_line = ""
errors_counter = 0
previous_line = ""  # Variable storing the previously read line of the logfile
log_time = ""
sw_rev_line = ""
up_time_line = ""

# TODO Use another loop and .rstrip() to remove all blank lines from the file
with open(file_path) as file_object:
    # Looping through the file and reading each line
    for line in file_object:
        # Breaking out of the loop after the useful section of the logs is checked,
        # in this way we don't check the whole file unnecessarily,
        # ~1300 lines of logs are read instead of ~20000
        if 'Bottom of Log :' in line:
            break
        for error_element in critical_errors_list:  # find and store critical errors
            if error_element in line:
                errors_counter += 1
                criticals_found.append(line)

        # Finding useful information about the device - not related to errors or warnings
        if 'Up Time' in line:
            # If the desired string is found in the line we set the variable's value to the line of the log
            up_time_line = line
            # REGEX is used to extract only the meaningful information from the line of text
            up_time = re.search(r"\d+\s\w+", up_time_line)
        if 'Software revision' in line:
            sw_rev_line = line
            software_rev = re.search(r"\w{2}[.]\w+[.]\w+[.]\w+", sw_rev_line)
        if 'show time' in previous_line:
            log_time = line
        # Gets the product number of the device - also needed for the "USEFUL LINKS" section
        if 'Product:   HP J' in line:
            product_n_line = line
            product_number = re.search(r"[J]\w\d{3}\w", product_n_line)

        # Example warning/major messages:
        # W 10/25/13 17:42:51 00374 chassis: WARNING: SSC is out of Date: Load 8.2 or
        #           newer
        # M 03/07/18 08:48:32 02796 chassis: AM1: Internal power supply 1 inserted.
        # All messages start with a letter indicating severity and then the date/time of the error
        # Warnings start with 'W', major errors with 'M'. Some messages are on one line, others are on two lines.
        # If the message is on two lines, the second line always starts with whitespace
        # These messages are caught with "[W]\s\d"
        # The second if looks if the next message starts with whitespace
        if re.search(r"[W]\s\d", previous_line):
            warning = previous_line
            warnings_found.append(warning)
            if re.search(r"[\s]", line):
                second_warning = line
                warnings_found.append(second_warning)

        # At the end of the loop we use the previous_line variable to store the line of text before the next line of log
        # is checked.
        previous_line = line

print()
# Print useful device information
print("#################################")
print(f"USEFUL SWITCH INFORMATION: ")
print("#################################")
print()
print(f"Log generated on: {log_time.rstrip()}")
print(f"Software revision: {software_rev.group()}")
print(f"Up time: {up_time.group()}")
print(f"Product number: {product_number.group()}")
print()
print()

# Print useful links
print("#################################")
print(f"USEFUL LINKS: ")
print("#################################")
print("Order a replacement part:")
print(f"http://partsurfer.hpe.com/Search.aspx?SearchText={product_number.group()}")
print("Download the latest software:")
print(f"https://h10145.www1.hpe.com/downloads/SoftwareReleases.aspx?ProductNumber={product_number.group()}")
print()
print()
# Print the message if critical errors are found in the logfile.
print("#################################")
print(f"Critical errors found in logfile:")
print("#################################")
print()
if errors_counter == 0:
    print('No critical errors were found in the logfile.')
else:
    print(*criticals_found)
    print()
    print('Possible replacement needed.')
    print()

# Print the list of warnings
print("#################################")
print(f"Warnings found:")
print("#################################")
print(*warnings_found)

# Printing time taken to analyze the log (for testing purposes)
# print("--- %s seconds ---" % (time.time() - start_time))
print(f"Time taken: {time.time() - start_time:.3f} sec.")

