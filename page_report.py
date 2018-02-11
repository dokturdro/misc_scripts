import sys
import re

# Regular expression isolating the desired part of a string #
pattern=re.compile('^\d+\.\d+\.\d+\.\d+\s\[[0-3]\d/(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/20\d\d:[0-2][0-9]:[0-5][0-9]:[0-5][0-9]\s\+[0-1][0-9]00\]\s\"GET http://((?:[a-z]+\.)+[a-z]+(?:/[a-z]+)*).*\sHTTP/\d\.\d\"\s\d+\s\d+$')

# Dictionary holder for possible invalid lines #
address_count = {'Invalid log lines' : 0}

# Setup of a loop running the regular expression through lines in the file #
for line in file.readlines():
    match_set = pattern.match(line)
    try:
        match = match_set.group(1) # Check if string is already parsed #
        if match in address_count: # If it is: add 1 to counter #
            address_count[match] += 1
        else:                          # If it is not: set a new key #
            address_count[match] = 1


    except AttributeError: # Not fitting lines add 1 to invalid caunter #
        address_count['Invalid log lines'] += 1

# Setup of a loop writing down the results in desired location and format #
for key in sorted(address_count):

    if key == "Invalid log lines": # Write to stderr #
        output = "\"" + key + "\"" + "," + str(address_count[key]) + "\n"
        sys.stderr.write(output)
    else: # Write to stdout "
        output = "\"" + key + "\"" + "," + str(address_count[key]) + "\n"
        sys.stdout.write(output)

file.close()
