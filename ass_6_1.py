for letter in 'banana':
    print(letter)
s = 'Money Python'
print(s[0:4])
print(s[4:7])
print(s[6:])

text = "X-DSPAM-Confidence:    0.8475"
dir(text)
colonLocation = text.find(":")
print(colonLocation)

number = (text[colonLocation+1:])
number = float(number)
print(number)

