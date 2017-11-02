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
import decimal
def frange(start,stop = None,step=0.25):
    step = decimal.Decimal(str(step))

    if stop is None:
        stop = decimal.Decimal(str(start))
        curr = decimal.Decimal(0.0)
    else:
        stop = decimal.Decimal(str(stop))
        curr = decimal.Decimal(str(start))

    if step!= 0:
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
