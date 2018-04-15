# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

import xlsxwriter

# Init workbook/worksheet
filename = "yelpscrap.xlsx"
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()

# -- Page Title
row = 0; col = 0
worksheet.write(row, col, "List of Shops")

# -- Headers
row = 1; col = 0
heads = ("Shop name", "Address", "ZipCode", "District", "Phone", "Categories")
for head in heads:
    worksheet.write(row, col, head)
    col += 1
workbook.close()
