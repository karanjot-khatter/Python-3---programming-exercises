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
#Program display a single card
import showcard
def main():
    number = input("Pick a card(1-52):")
    filename = "BMP" + number + ".GIF" #in question BMPn.Gif
    showcard.set_timeout(10) #normal timeout is 5 - changed this
    showcard.display_file(filename) #in question


main()