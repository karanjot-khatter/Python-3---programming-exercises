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
from math import pi, tan, cos
def main():
    elevation = 80
    barrelH = 1
    distanceH = 0.5
    initalV = 44
    acceleration = 9.81

    theta = elevation * pi / 180

    y = barrelH  + distanceH * tan(theta)
    y2 = (acceleration * barrelH**2) / (2*(initalV* cos(theta) **2))
    height = y - y2
    print(height)

main()