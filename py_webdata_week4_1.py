import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sumval = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sumval = sumval + int(tag.contents[0])

print(sumval)







exit(-1)

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1225044.html'
#fhand=urllib.request.urlopen('https://www.dph.illinois.gov/covid19/covid19-statistics')
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
html = urllib.request.urlopen('http://www.dr-chuck.com/page-1.htm').read()
#html = urllib.request.urlopen('https://www.dph.illinois.gov/covid19/covid19-statistics').read()
soup = BeautifulSoup(html, 'html.parser')
#properties = soup.findAll('a', onclick=True)
#print(properties)
#exit(0)

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode('UTF-32')
#print(cmd.decode('UTF-32'))


counts = dict()
for line in fhand:
    #print(line)
    #print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(ord('l'), ord('i'), ord('n'), ord('e'))
print(ascii(108), ascii(105))
#print(counts)
#<a href="#" onclick="PopulateZipMap(); return false;">By Zip</a>
#<a href="#" onclick="populateMap(); return false;">By County</a>
#function populateMap(selectedDate)