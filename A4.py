# We prompt the users to enter two numbers A and B
A = int(input("Enter A: "))
B = int(input("Enter B: "))
# We check if both of them are binary i.e if they both are either zero or one only and display error message if not binary
if (A == 0 or A == 1) and (B == 0 or B == 1):
    # We further check each case of values of A and B and then decide their AND OR and XOR values
    if A == 1 and B == 1:
        print("AND = 1")
        print("OR = 1")
        print("XOR = 0")
    elif A == 0 and B == 0:
        print("AND = 0")
        print("OR = 0")
        print("XOR = 0")
    elif A == 1 and B == 0:
        print("AND = 0")
        print("OR = 1")
        print("XOR = 1")
    elif A == 0 and B == 1:
        print("AND = 0")
        print("OR = 1")
        print("XOR = 1")  
else:
    print("Bits must be 0 or 1")
