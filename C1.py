#We define two functions
def ohms_current(v,r):
    #Calculates the Current using the two parameters of the function and then return this value
    I = v/r
    return I
def power_dissipated(i,r):
    #Calculates the power using the two parameters of the function and then return this value
    P = (i**2)*r
    return P
# setting Voltage to 12V and Resistance to 6 ohms
V = 12
R = 6
# calling the functions with our values that we set and then stroing these values in variables and then later printing these variables
Current = ohms_current(V,R)
Power = power_dissipated(Current,R)
print("Current =",Current ,"A")
print("Power =",Power,"W")
