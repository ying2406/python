import os
import random

mapnaam = input("How would u like to name your folder? ")

lengte_mapnaam = len(mapnaam)

if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + " is made, enjoy!.")

else:
    print("you did not type anything")