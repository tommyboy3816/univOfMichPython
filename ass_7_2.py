# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1.0
    line = line.rstrip()
    val = float(line.split(" ")[1])
    total = total + val

print("Average spam confidence: " + str(total / count))
