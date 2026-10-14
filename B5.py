# Prompt the user to enter the resistor's value and initialse the 1% tolerance and the 5% tolerance counter and the reject counter to 0
R = int(input("Enter the value of resistor: "))
t1 = 0
t5 = 0
reject = 0
# We make sure that the loop only runs when the user enters a non zero value or else the loop exits. We catagorise the values of tolerance in the loop by using if and else statements and then sort the category of the resistor
while R != 0:
    if  R >= 95 and R<= 105:
        if R >= 99 and R <= 101:
            t1 += 1
        else:
            t5 += 1
    else:
        reject += 1
    R = int(input("Enter the value of resistor: "))
#Now we print the number of resistors that fall in each category
print("Number of 1% tolerance resistors are:",t1)
print("Number of 5% tolerance resistors are:",t5)
print("Number of rejected resistors are:",reject)        
            
