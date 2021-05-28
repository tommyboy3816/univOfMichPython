hist = dict()
count = 0

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    count+=1
    #print("line = %s" % line)
    line = line.strip()

    if line.startswith("From:") is True:
        continue
    if line.startswith("From") is True:
        #print(line)
        info = line.split()
        person = info[1]
        hist[person] = hist.get(person,0) + 1

for y in hist:
    print(y)
print(hist.values())
keys = list(hist.keys())

maxval = 0
maxperson = None

for key in keys:
    if hist[key] > maxval:
        maxval = hist[key]
        maxperson = key

print(maxperson, maxval)

