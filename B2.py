# We ask the user how many resistors that are in series
num = int(input("How many resistors? "))
Total = 0
# We use a for loop to add the number of resistances entered by the user and then print the total i.e total resistance in series
for i in range(num):
    R = int(input("Enter R: "))
    Total += R
print("Total Resistance =", Total,"Ohms") 
    
