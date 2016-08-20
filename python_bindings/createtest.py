import numpy as np

f = open("test.txt","w")
d = 1
m = 9
y = 2016
count = 0
while y<2019:
    if d<31:
        f.write(str(d))
        f.write(" ")
        if m<13:
            f.write(str(m))
            f.write(" ")
            if y<2019:
                f.write(str(y))
                f.write("\n")
                d = d + 1
        else:
            m=1
            y += 1
    else:
        m = m+1
        d=1
f.close()