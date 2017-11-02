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

def myfunc(value, alist= None):
    if alist == None: alist = []
    alist.append(value)
    print("Value of a list is", alist)
myfunc(42)
myfunc(27)
myfunc(99)