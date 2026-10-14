# We ask the users to enter three resistances R1, R2 and R3
R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))
# Now we compare one selected resistance with others and check which one is the largest and then print that value
if R1 > R2 and R1 > R3:
    print("Largest =",R1)
elif R2 > R1 and R2 > R3:
    print("Largest =",R2)
else:
    print("Largest =",R3)
# Now we compare one selected resistance with others and check which one is the smallest and then print that value   
if R1 < R2 and R1 < R3:
    print("Smallest =",R1)
elif R2 < R1 and R2 < R3:
    print("Smallest =",R2)
else:
    print("Smallest =",R3)
