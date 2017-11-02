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
#check size of file, use len() built in. __len__
import os.path
class MyFile(object):

    def __init__(self,filename):
        self.__fname = filename

    def __str__(self):
        s = open(self.__fname).read()
        return s

    def __len__(self):
        return os.path.getsize(self.__fname)

    def get_fname(self):
        return self.__fname
