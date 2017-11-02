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
#this implements the enchancement to accept a single paramater
def frange(start,stop = None,step=0.25):
    if stop is None:
        stop = start
        curr = 0.0
    else:
        curr = float(start)

    #taken from last exercises
    while curr < stop:
        yield curr
        curr +=step

one = list(frange(0,3.5,0.25))
two = list(frange(3.5))
if one ==two:
    print("Defaults worked")
else:
    print("Oops! Defautls did not work")
    print("one:", one)
    print("two:", two)