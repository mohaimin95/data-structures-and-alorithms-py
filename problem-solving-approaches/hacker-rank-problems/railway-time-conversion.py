def timeConversion(s):
    segments = s.split(":")
    is_evening = "PM" in segments[2]
    if segments[0] == "12":
        segments[0] = "00"
    if is_evening:
        segments[0] = str(int(segments[0]) + 12)

    return ":".join(segments).replace("AM", "").replace("PM", "")


print(timeConversion("07:05:45PM"))
print(timeConversion("12:05:45PM"))
print(timeConversion("12:05:45AM"))
print(timeConversion("01:05:45AM"))
