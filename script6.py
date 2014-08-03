#!/usr/bin/python
# create html table from csv
# Author(s): Chris Trombley <ctroms@gmail.com>
# Version 2 - added css class to all columns except header

#!/usr/bin/python
# create html table from csv

import os
import sys
import csv
import ftplib
from ftplib import FTP

#sys.argv = ['script4.py', 'test3.csv', 'out.html']
 
if len(sys.argv) < 3:
	print "Usage: csvToTable.py csv_file html_file"
	exit(1)

# Open the CSV file for reading
reader = csv.reader(open(sys.argv[1]), delimiter = '|')

# Create the HTML file for output
htmlfile = open(sys.argv[2],"w")

# initialize rownum variable
rownum = 0

# write <table> tag
htmlfile.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

        "http://www.w3.org/TR/html4/loose.dtd">



<html lang="en">



<head>



	<meta http-equiv="content-type" content="text/html; charset=utf-8">

	<title>Buy Signals</title>

<link href="http://www.advancedmomentuminvesting.com/templates/gantry/css/FooTablecss/footable.core.css" rel="stylesheet" type="text/css" />
<link href="http://www.advancedmomentuminvesting.com/templates/gantry/css/FooTablecss/footable.standalone.css" rel="stylesheet" type="text/css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js" type="text/javascript"></script>
<script src="http://www.advancedmomentuminvesting.com/templates/gantry/js/footable.js" type="text/javascript"></script>
<script src="http://www.advancedmomentuminvesting.com/templates/gantry/js/footable.sort.js" type="text/javascript"></script>



</head>



<body>
<table class="footable">
  <thead>
    <tr>
      <th data-type="alpha">Symbol</th>
      <th data-hide="phone,tablet" data-type="alpha">Company Name</th>
      <th data-hide="phone,tablet" data-type="alpha">Equity Type</th>
	  <th data-hide="phone,tablet" data-type="alpha">Exchange</th>
	  <th data-type="alpha">Sector</th>
	  <th data-hide="phone,tablet" data-type="alpha">Industry</th>
	  <th data-type="numeric">Price</th>
	  <th data-hide="phone,tablet" data-type="numeric">52 Week Low</th>
	  <th data-hide="phone,tablet" data-type="numeric">52 Week High</th>
	  <th data-hide="phone,tablet" data-type="numeric">Market Cap MM</th>
	  <th data-hide="phone,tablet" data-type="numeric">PE Ratio</th>
	  <th data-hide="phone,tablet" data-type="numeric">Dividends Paid</th>
	  <th data-hide="phone,tablet" data-type="numeric">Purchase By Date</th>
    </tr>
  </thead>
  <tbody>''')

# generate table contents

# Read a single row from the CSV file
for row in reader: 

	# write header row. assumes first row in csv contains header
	#if rownum == 0:
	#	htmlfile.write('<tr>') # write <tr> tag
  	#	for column in row:
  	#		htmlfile.write('<th>' + column + '</th>')
  	#	htmlfile.write('</tr>')

  	#write all other rows	
  	#else:
	htmlfile.write('<tr>')	
	for column in row:
		htmlfile.write('<td>' + column + '</td>')
	htmlfile.write('</tr>')
	
	#increment row count	
	rownum += 1

# write </table> tag
htmlfile.write('''</tbody>
</table>



  

<script type="text/javascript">
	$(function () {
		$('.footable').footable();
	});
</script>

</body>



</html>''')

# close output file
htmlfile.close()

# print results to shell
print "Created " + str(rownum) + " row table."

# ftp file to server
ftp = FTP('ftp.advancedmomentuminvesting.com')

print "Logging in:"
ftp.login('admin@advancedmomentuminvesting.com', '')
print ftp.getwelcome()

# change directory
ftp.cwd('/www/update/')
print ftp.pwd()
print ftp.nlst('/www/update/')



# define upload 
def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

# choose server, file and upload		
upload(ftp, "out.html")

print ftp.nlst('/www/update/')

ftp.quit()

exit(0)