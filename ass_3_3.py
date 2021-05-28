score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("EXCEPTION: score = %s" % score)
    score = -1

if score != -1:
    if score > 1.0:
        print("INVALID input: %f" % score)
    elif score > 0.9:
        print("A")
    elif score > 0.8:
        print("B")
    elif score > 0.7:
        print("C")
    elif score > 0.6:
        print("D")
    elif score < 0.0:
        print("INVALID input: %f" % score)
    else:
        print("F")
else:
    print("INVALID input: %s" % score)
