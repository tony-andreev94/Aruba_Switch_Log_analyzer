# HPN_L1_Tool
This is a repository for a CLI based switch log analyzer application. It is used to help L1 engineers with logfile analysis of "Aruba" or traditional "ProCurve" switches.
The application takes a diagnostics file as an input, loops through each line of the file and provides the following information: 
 - All critical messages indicating there is a hardware issue.
 - All warnings messages contained in the device's logbuffer.
 - General device information including:
   * Device's uptime
   * Used software version
   * Device's product number
   * Device's serial number
 - Useful links where newer software versions can be downloaded or a list of available parts can be found.

# Future plans:
- Use Django to make the project a web application with a browse button allowing the user to select a specific logfile to be analyzed.
- Use web scraping to check if the device's software version is among the supported versions.

# "TO-DO"s:
- Basic error handling:
  - Check if the input file is a text file - if the extension is ".log" or ".txt" (in FileLoader class)
  
  - Check if the text file is indeed a logfile - if the "show tech all" command is present. (in Analyzer class)

- Add time taken for execution.
