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

def main():
    year = int(input("Please enter a year:"))
    if year % 4 and not year % 100:
        print(year,"is a leep year")
#    elif year % 400 == 0:
    #    print(year, "is a leep year")
    else:
        print(year, "is not a leep year")
main()