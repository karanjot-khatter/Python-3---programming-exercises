#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     30/10/2017
# Copyright:   (c) Admin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
def main():
    argc = len(sys.argv)
    #character more than one than this runs
    if argc > 1:
        print("Too many args")
    #otherwise run this
    else:
        where = "World"
        print("Hello", where)

    print("Goodbye from " + sys.argv[0])
main()
