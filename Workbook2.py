# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import xlsxwriter
import re
from datetime import datetime


# Init workbook/worksheet

# current datetime string
now=str(datetime.now())

#strip out chars from now
striped=re.sub('[^0-9]+','',now)

# append filename with datestamp
filename = "yelpscrap-"+striped+".xlsx"
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()

row = 0
col = 0
worksheet.write(row, col, "Shops List")

# -- Headers
row = 1; col = 0
heads = ("Shop name", "Address", "ZipCode", "District", "Phone", "Categories")
for head in heads:
    worksheet.write(row, col, head)
    col += 1
workbook.close()
