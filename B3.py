#Initialising our list readings and storing a few values in it
readings = [3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]
#set highest and lowest to the first value of the list as a reference reading for comparison and initialize total with this value and set above(readings above 3.2) counter to 0
highest = readings[0]
lowest = readings[0]
total = readings[0]
above = 0
# Start the loop from the second value of the list since we already have set the highest and lowest to the first so we compare with the nect value
for i in range(1,len(readings)):
    if readings[i] > highest:
        highest = readings[i]
    if readings[i] < lowest:
        lowest = readings[i]
    total += readings[i]
    if readings[i] > 3.2:
        above += 1
# Now we calculate the average through the total and the number of values in our list and then print the readings above 3.2, highest, lowest and average
average = round((total/ len(readings)),2)
print("Readings above 3.2 V: ", above)
print("Highest: ",highest)

print("Lowest: ",lowest)
print("Average: ",average)
