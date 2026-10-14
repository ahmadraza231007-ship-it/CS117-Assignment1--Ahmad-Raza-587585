# We prompt the user to input the colour of the first band of resistor
colour = input("Please enter the colour of the first band of the resistor: ")
#We check if the colour is amongst the acceptable values or not and if it is, then we print the value of that colour
if colour.lower() == "black":
    print("Digit = 0")
elif colour.lower() == "brown":
    print("Digit = 1")
elif colour.lower() == "red":
    print("Digit = 2")
elif colour.lower() == "orange":
    print("Digit = 3")
elif colour.lower() == "yellow":
    print("Digit = 4")
elif colour.lower() == "green":
    print("Digit = 5")
elif colour.lower() == "blue":
    print("Digit = 6")
elif colour.lower() == "viloet":
    print("Digit = 7")
elif colour.lower() == "grey":
    print("Digit = 8")
elif colour.lower() == "white":
    print("Digit = 9")
else:
    print("Invalid colour")
    


          

