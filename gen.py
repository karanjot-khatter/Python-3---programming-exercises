#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     01/11/2017
# Copyright:   (c) Admin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def frange(start,stop,step=0.25):
    curr = float(start)
    while curr<stop:
        yield curr
        curr += step

print(list(frange(1.1,3)))
print(list(frange(1.1,3,0.33)))
print(list(frange(1.1,31)))
print(list(frange(3,1)))
print(list(frange(-1, -0.5, 0.1)))

for num in frange(3.142, 12):
    print(f"{num:05.2f}")


print(frange(1,2))