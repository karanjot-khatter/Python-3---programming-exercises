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
    var = input("Please enter an interger: ")
    if var.isdecimal():
        var = int(var)
        for i in range(var,-1,-2):
            print(i)
    else:
        print("error")
        sys.exit



main()
