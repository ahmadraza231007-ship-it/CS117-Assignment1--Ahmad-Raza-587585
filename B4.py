#Initialize the list voltages to some values, longest and current to 1, start, first and last to zero
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
longest = 1
current = 1
start = 0
first = 0
last = 0
#We start the loop's counter with second index of list and then compare it with the previos vlaue of the list (i-1) and if the value is smaller than previous, we increment current but if at any point the next value of list is not smaller, we set current back to 1 and now start is equal to i. Then we check if the current streak is the longest and if it is, we set first to start which was the index of the first element of the longest streak and set last to i which is the index of the last element in the streak.
for i in range(1,len(voltages)):
    if voltages[i] < voltages[i-1]:
        current += 1
    else:
        current = 1
        start = i
    if current > longest:
        longest = current
        first = start
        last = i
# Now we print the longest streak's length, the first value of this streak and the last value of this streak
print("Longest streak:", longest, "readings")
print("Started at:", voltages[first],"V")
print("Ended at:", voltages[last], "V")
