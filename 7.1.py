#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     31/10/2017
# Copyright:   (c) Admin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

if sys.platform == 'win32':
    file = r'C:\WINDOWS\system32\drivers\etc\services'
else:
    file = '/etc/services'

count = 1

for line in open(file, 'r'):

   if line[0:1] != '#' and not line.isspace():
       name, pp = line.split(None, 1)
       port, protocol = pp.split ('/', 1)

       port = int(port)
       while count < port:
           print ("Unused port: " + str(count))
           count += 1
           if count > 200: break

       count = int(port) + 1
       if count > 200: break
