# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

for ii in range(count):
   print("Retrieving: {}".format(url))
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')

   jj = 1

   # Retrieve all of the anchor tags
   tags = soup('a')
   for tag in tags:
       url = tag.get('href', None)
       if jj == pos:
           break
       jj = jj + 1


print("Retrieving: {}".format(url))


#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Eirinn.html'