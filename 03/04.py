seconds = -10
hours = None

if seconds >= 60:
    print("More than a minute")
    if seconds >= 3600:
        print("More than an hour")
    seconds = seconds % 60
    hours = True
elif seconds == 0:
    print("Seconds is zero")
elif seconds < 0:
    print("Seconds is negative")
else:
    print("Seconds is positive and less than a minute")

print("Seconds:", seconds)
print("Hours:", hours)
