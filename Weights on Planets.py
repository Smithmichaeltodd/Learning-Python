#This program calculates your weights on other planets/celestial bodies
#Weights on Planets.py
#By Michael Smith

print ("       Welcome to planet calculator v 1.1\n")

print("       A)Weight on the Moon:")
print("       B)Weight on Mars:")
print("       C)Weight on the Sun:")
print("       D)Weight on Venus:")
print("       E)Press Enter to Exit:\n")

choice = input("       Pick your calculation:  ")

loop = "True"
while True:

    if choice == "A":
        X = eval(input("       Enter your weight in pounds:  "))

        print("       Your weight is:  " +str(((X/2.2046)*1.622)/9.81), "kgs\n")

        print("       A)Weight on the Moon:")
        print("       B)Weight on Mars:")
        print("       C)Weight on the Sun:")
        print("       D)Weight on Venus:")
        print("       E)Press Enter to Exit:\n")

        choice = input("       Pick your calculation:  ")


    if choice == "B":
        X = eval(input("       Enter your weight in pounds:  "))

        print("       Your weight is:  " +str(((X/2.2046)*3.77)/9.81), "kgs\n")

        print("       A)Weight on the Moon:")
        print("       B)Weight on Mars:")
        print("       C)Weight on the Sun:")
        print("       D)Weight on Venus:")
        print("       E)Press Enter to Exit:\n")

        choice = input("Pick your calculation:  ")


    if choice == "C":
        X = eval(input("       Enter your weight in pounds:  "))

        print("       Your weight is:  " +str(((X/2.2046)*274.13)/9.81), "kgs\n")
        print("       A)Weight on the Moon:")
        print("       B)Weight on Mars:")
        print("       C)Weight on the Sun:")
        print("       D)Weight on Venus:")
        print("       E)Press Enter to Exit:\n")

        choice = input("       Pick your calculation:  ")


    if choice == "D":
         X = eval(input("       Enter your weight in pounds:  "))

         print("       Your weight is:  " +str(((X/2.2046)*3.77)/8.87), "kgs\n")
         print("       A)Weight on the Moon:")
         print("       B)Weight on Mars:")
         print("       C)Weight on the Sun:")
         print("       D)Weight on Venus:")
         print("       E)Press Enter to Exit:\n")

         choice = input("       Pick your calculation:  ")

    if choice == "E":
        break

    if choice != "A" or "B" or "C" or "D" or "E":
        print("       Invalid option!\n")

        print("       A)Weight on the Moon:")
        print("       B)Weight on Mars:")
        print("       C)Weight on the Sun:")
        print("       D)Weight on Venus:")
        print("       E)Press Enter to Exit:\n")

        choice = input("       Pick your calculation:  ")






