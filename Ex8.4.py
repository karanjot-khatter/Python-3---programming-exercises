#!/usr/local/bin/python
import re

def prep_row (row):
    row = row.rstrip() # a - get rid of space / new lines
    row = re.sub(r"'",r"''",row) #single quote characters be double quoted (b)

    # Add quotes around each field
    #lrow = list((map (lambda f: "'"+f+"'", row.split(','))))

    lrow = []

    #c - all values must be enclosed in single quotes
    for field in row.split(','):
        lrow.append("'" + field + "'")

    return ",".join(lrow)


for row in open ("country.txt"):
    print (prep_row(row))

