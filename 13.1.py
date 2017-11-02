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
import subprocess
import os
import sys

#(a) - pyton rogram client.py from another, psasig a filename - words
proc = subprocess.run([sys.executable, 'client.py', 'words'])
print("Child exited with", proc.returncode)

#(b) - use pipe + capture output list.
proc = subprocess.run([sys.executable, 'client.py', 'words'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.stderr != None:
    print("error:", proc.stderr.decode())

print("output:", proc.stdout.decode())