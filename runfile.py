#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     02/11/2017
# Copyright:   (c) Admin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from myfile import MyFile

filea = MyFile('country.txt')
print(filea)

print(filea.get_fname(), "is", len(filea), "bytes")