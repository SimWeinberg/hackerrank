# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    list = s.split(":")
    if list[2][2] == "P":
        list[0] = int(list[0]) + 12
        string = ":".join(str(e) for e in list)
        return(string)
    elif (list[2][2]) == "A" and (list[0] == "12"):
        # not picking up if and
        list[0] = 0
        string = ":".join(str(e) for e in list)
        return(string)
    else:
        string = ":".join(str(e) for e in list)
        return(string)
    
    
print(timeConversion('3:00:00PM'))