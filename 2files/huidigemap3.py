import io
import random

bestand = open("test.txt", "w")

bestand.write("Testing 3 2 1 . .");  

bestand.close()


bestand2 = open("test.txt", "r")

bestand2.write("error")