import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)

sum = 0
num_vals = 0

for line in handle:
    line = line.strip()

    # find all the numbers in a line
    nums = re.findall('[0-9]+',line)

    # ignore lines without numbers
    if len(nums) == 0:
        continue

    for num in nums:
        num_vals += 1
        sum = sum + int(num)

print("number of values {}".format(num_vals))
print("SUM is {}".format(sum))
