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

def fuelRequirement():
    fuelperLap = 2.25
    min = 45 * fuelperLap
    print("During a 45 lap race, the minumum fuel requirement is", min)

    #Typically a ar will carry an extra 50 % contigency
    fuel = min * 1.5 #multiply min by 1.5
    print("Full fuel load:", fuel, "kg")

    #qualify lap = 80.45s
    #with 5kg of fuel
    #each 10kg of fuel decreases the lap by 0.35s

    QlapTime = 80.45

    #inital lap time would be
    TlapTime = QlapTime - (0.35/10 * 5)
    print("Therotetical inital lap time:", TlapTime)

    lapOneTime = TlapTime + ((fuel/10) * 0.35)
    print("lap one time:", lapOneTime, "seconds")
fuelRequirement()