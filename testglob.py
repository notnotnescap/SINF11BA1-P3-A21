
i = 9
c = "00000:00090:00000:00000:00000"
if c[i-1] == ":":
    c = c[:i-2] + "9:" + "0" + c[i+1:]
    print(c, "premier")
else:
    c = c[:i-2] + "9" + "00" + c[i+1:]
    print(c, "deux")
