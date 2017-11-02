

import os
start_time = 0;

def start_timer():
    global start_time
    (utime,stime) = os.times()[0:2]
    start_time = utime+stime

def end_timer(txt='End time'):

    (utime,stime) = os.times()[0:2]
    end_time = utime+stime
    print ("{0:<12}: {1:01.3f} seconds".
        format(txt,end_time-start_time))

start_timer()
lines = 0
for row in open ("words"):
    lines += 1

end_timer()
print ("Number of lines:",lines)