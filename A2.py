# we prompt the user to enter the value of current
current = int(input("Please enter the value of current: "))
# We check if current is zero, positive or negative and then in each case decide the path
if current == 0:
    print("No current flows")
elif current > 0:
    print("Current flows from A to B")
else:
    print("Current flows from B to A")
    
            
