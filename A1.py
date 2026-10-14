# We take the voltage and resistance as input from the user
V = int(input("Please enter the voltage: "))
R = int(input("Please enter the resistance: "))
# We only calculate the current if Resistance is greater than zero or else output error message. We check if current is greather than 2 or not
if R > 0:
    I = V/R
    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
else:
    print("Invalid resistance")
