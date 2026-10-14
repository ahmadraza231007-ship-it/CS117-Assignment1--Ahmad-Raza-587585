# We define our function star to delta and take three resistances as parameters: Ra, Rb and Rc
def star_to_delta(ra, rb, rc):
    # We first calculate R numerator using our formula
    Rnum = (ra*rb) + (rb*rc) + (rc*ra)
    # Now we individually calculate Rab, Rbc and Rca using our formula and then round all these values to 2 decimal places
    Rab = round(Rnum/rc,2)
    Rbc = round(Rnum/ra,2)
    Rca = round(Rnum/rb,2)
    # We return Rab, Rbc and Rca values from our function
    return Rab, Rbc, Rca
# We prompt the user to enter the three resistances Ra, Rb and RC and then we print Rab, Rbc and Ra by calling our function with the paramaters user entered
Ra = float(input("Enter resistance Ra: "))
Rb = float(input("Enter resistance Rb: "))
Rc = float(input("Enter resistance Rc: "))
print("The equivalent Delta network resistances are:",star_to_delta(Ra, Rb, Rc)) 
