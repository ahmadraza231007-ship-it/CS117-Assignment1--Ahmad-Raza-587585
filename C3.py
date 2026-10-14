#we define our funtion that converts decimal to binary and takes a number as a parameter
def decimal_to_binary(n):
    # We make a list named binary that stores the remainder after each calculation in each index
    binary = []
    # we divide our number by 2 again and again until zero is reached
    while n != 0:
        #calculating remainder and storing it on our list
        rem = str(n%2)
        binary.append(rem)
        # now our number is equal to the number after dividing it by 2
        n = n//2
    # we initialise a string named ans to "" which means it stores no value yet but it's a string
    ans = ""
    # now we run our list from the bottom to the top as the rule is for binary conversion and every element of the list is added to ans
    for i in range(len(binary)-1,-1,-1):
        ans += binary[i]
    # we return ans which is basically the binary number
    return ans
# now we ask a user to enter a number to convert into binary, then call this number on our function and store it's value in a variable and then finally print this variable and output the binary number
num = int(input("Please enter a number to convert to binary: "))
answer = decimal_to_binary(num)
print("The binary answer is: ", answer)
    

        
