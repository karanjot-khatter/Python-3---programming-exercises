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
    firstName = input("Please enter your first name:")
    surname = input("Please enter your surname:")
    print(firstName,surname)
    print([firstName,surname])

    dictionary ={"forname" : firstName, "surname": surname}
    print(dictionary)
main()