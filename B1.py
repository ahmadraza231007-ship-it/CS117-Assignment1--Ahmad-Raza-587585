# We set the value of Resistance to 10 ohms by ourself
R = 10
# We will run the loop from Voltage = 1v to Voltage = 10v and calculate corresponding current values using our fixed resistance and then print these values
for V in range(1,11):
    I = V/R
    print("V =",V,"V, I =",I,"I")
