import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = 'http://py4e-data.dr-chuck.net/comments_42.json'
address = 'http://py4e-data.dr-chuck.net/comments_1225047.json'
#address = input('Enter location: ')
if len(address) < 1:
    exit(-1)

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        exit(-1)

sumval = 0

for item in js["comments"]:
    #print(item)
    sumval = sumval + item["count"]

print("Count: {}".format(len(js["comments"])))
print("Sum: {}".format(sumval))


exit(0)

data = '''{
          "name":"Luke",
          "phone":{
             "type":"intl",
             "number":"5764797"
             },
          "email":{
             "hide":"yes"
             }
          }
       '''
input = '''
          [
          {
             "id"   : "001",
             "x"    : "2",
             "name" : "Luke"
          },
          {
             "id"   : "009",
             "x"    : "7",
             "name" : "Pete"
          }
          ]
'''
info = json.loads(data)
#print('Name:', info["name"])
#print('Hide:', info["email"]["hide"])

info2 = json.loads(input)
print('user count {}'.format(len(info2)))
for item in info2:
    print('Name', item["name"])
    print('ID', item['id'])
    print('x', item['x'])
