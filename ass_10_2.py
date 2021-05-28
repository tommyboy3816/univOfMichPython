name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


hours = dict()

for line in handle:
    line = line.strip()

    if line.startswith("From:") is True:
        continue
    if line.startswith("From") is True:
        From, email, day, month, date, time1, year = line.split()
        hour, min, sec = time1.split(":")
        hours[hour] = hours.get(hour,0) + 1

for k,v in sorted(hours.items()):
    print(k,v)
