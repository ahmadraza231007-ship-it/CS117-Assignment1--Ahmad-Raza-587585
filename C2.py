# defining a parallel resistance funtion that calculates equivalent resistance of a prallel combination and takes a list as it's parameter
def parallel_resistance(resistors):
    reciprocal = 0
    #We take each resistance from the list and then use our formula to calculate equivalent resistance
    for i in range(len(resistors)):
        reciprocal += (1/resistors[i])
    Req = 1/reciprocal
    # We return the R equivalent
    return Req
#We initialize the list and then we ask the user to enter as many values of parallel resistors and enter 0 to start the calculation
resistor = []
R = int(input("Plese enter the resistance of each resistor. Enter 0 to terminate: "))
while R != 0:
    resistor.append(R) 
    R = int(input("Plese enter the resistance of each resistor.Enter 0 to terminate: "))
#Now we call our function and save it's value in a variable and then print this variable to output the equivalent resistance
EquivalentR = parallel_resistance(resistor)
print("The equivalent resistance is: ",round(EquivalentR,3))
        
