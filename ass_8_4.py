fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    linelist = line.split()
    for word in linelist:
        if lst is None:
            lst.append(word)
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
