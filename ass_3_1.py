hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

pay = 0.0

if h > 40.0:
    pay = (1.5 * (h - 40.0)) * r + (40*r)
else:
    pay = h * r

print(pay)
