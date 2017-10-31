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
    Belgium = "Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German"
    items = Belgium.split(",")
    print ("-" * len(Belgium))
    print(":".join(items))
    print(int(items[1]) + int(items[3]))
main()