"""
Tian
Dec. 27
The program downloads the slides on comp215 website to the current dir or the designated dir
Need to install python (2.0 above) and beautifulsoup first
On Mac, simply type "easy_install beautifulsoup4" on terminal
further info about how to install beautifulsoup4 on https://www.crummy.com/software/BeautifulSoup/bs4/doc/

To run the program on Mac: 
1. open terminal
2. either type "python [absolute path]/comp215dl.py" or navigate to the source folder and type "python /comp215dl.py"
"""
import urllib2
import csv
import re
from bs4 import BeautifulSoup
# import sys

def download_file(download_url, file_name):
    response = urllib2.urlopen(download_url)
    file = open(file_name, 'w')
    file.write(response.read())
    file.close()
    print(file_name + " completed")

# extended later
dir = raw_input('************************************************\n'+
	'input the dir path you want to put the slides in.\nIf you have navigated to the destination dir,\nsimply input ".." (excluding the quotes):\n')
if (not dir.endswith("/")):
	dir = dir + '/'
rename = raw_input('************************************************\n'
	+'Rename the slides?\nIf you choose to rename,\nthe slides will be named "slide1," "slide2" '
	+'and so forth.\nType Q to quit the program\nY/N/Q: ')
rename = rename.lower()
print("************************************************")
# the class website url to be read
url = 'http://comp215.blogs.rice.edu/schedule/'
# fetch the html content
content = urllib2.urlopen(url).read()
# use soup
soup = BeautifulSoup(content, 'html.parser')

#the selected content, which are key-value tuples
aTuples = soup.find_all('a')

numberOfPdf = 1
if rename != 'q':
	for tuples in aTuples:
		if ('href' in tuples.attrs and tuples.attrs['href'].endswith('.pdf')):
			download_url = tuples.attrs['href']
			if (rename == 'y'):
				file_name = "slide"+str(numberOfPdf)+".pdf"
			else : 
				file_name = download_url[download_url.find('week'):len(download_url)]
			if (dir == ".." or dir == "/.." or dir == "../" or dir == "/../"):
				download_file(download_url, file_name)
			else :
				download_file(download_url, dir + file_name)
			numberOfPdf += 1

print("************************************************\nDone!")


