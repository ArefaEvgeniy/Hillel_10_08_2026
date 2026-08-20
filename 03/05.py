import this

seconds = 100
hours = True
text = ""
a = 10
b = 45
c = 0

if (seconds >= 60 or hours is True) or not (a > 5 and b < 50) and (c == 0):
    print("More than a minute")
    seconds = seconds % 60

print("Seconds:", seconds)
