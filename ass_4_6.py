def computepay(h,r):
    if( h > 40 ):
        return (h-40)*r*1.5 + (40*r)
    else:
        return h*r
print("fk")
exit(0)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

#hrs = int(hrs)
#rate = float(rate)

p = computepay( hrs, rate )
print("Pay",p)

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!!!')