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
import getpass
def main():
    pin = "0000"

    for tries in range(1,4):
        suppliedP = getpass.getpass("Enter your pin")
        if suppliedP == pin:
            print("well done, you remembered it")
            print("it only took", tries, "attempts")
        else:
            print("You had", tries, "tries and failed!")
main()