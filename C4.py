# we define our function loaded divider and take voltage source, R1, R2 and load resistance as our parameters
def loaded_divider(vs, r1, r2, rL):
    # we find out the voltage across R2 without considering Load resistance
    unloaded = (r2*vs)/(r1+r2)
    # We find equivalent resistance of R2 and Load Resistance
    Req = (rL*r2)/(rL+r2)
    # we find out the voltage across R2 considering Load resistance
    loaded = (Req*vs)/(Req+r1)
    # We return both the loaded and unloaded voltage drop
    return unloaded,loaded
# We ask the user to enter all the parameters seperately and then we put these parameters in our function and then output the values calculated by the function
Vs = int(input("Please enter the source voltage: "))
R1 = int(input("Please enter the Resistance of first resistor: "))
R2 = int(input("Please enter the Resistance of second resistor: "))
RL = int(input("Please enter the Resistance of load: "))
print("The unloaded and loaded voltages are: ", loaded_divider(Vs, R1, R2, RL))

