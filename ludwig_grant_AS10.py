# File Name: ludwig_grant_AS10.py
# File Path: /home/ludwigg/Python/PyRpi_AS10/ludwig_grant_AS10.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS10/ludwig_grant_AS10.py

# Grant Ludwig
# 10/25/2019
# AS.10
# Sort 3 numbers

points = 0

def min(num1, i1, num2, i2):
	global points
	if num1 < num2:
		points += 1
		return i1, i2
	else:
		points += 1
		return i2, i1

def sort(list):
	global points
	firstIndex = -1
	middleIndex = -1
	lastIndex = -1
	
	# compare index 0 & 1 and 1 & 2
	firstMinIndex, firstMaxIndex = min(list[0], 0, list[1], 1)
	secondMinIndex, secondMaxIndex = min(list[1], 1, list[2], 2)
	
	if firstMinIndex == secondMinIndex:
		points += 1
		firstIndex = firstMinIndex
		middleIndex, lastIndex = min(list[firstMaxIndex], firstMaxIndex, list[secondMaxIndex], secondMaxIndex)
	else:
		points += 1
		firstIndex, middleIndex = min(list[firstMinIndex], firstMinIndex, list[secondMinIndex], secondMinIndex)
		if firstMaxIndex != secondMinIndex and firstMaxIndex != secondMaxIndex:
			points += 2
			lastIndex = firstMaxIndex
		else:
			points += 2
			lastIndex = secondMaxIndex
		
	return [list[firstIndex], list[middleIndex], list[lastIndex]]

listOfList = ((1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1))
for list in listOfList:
	sorted = sort(list)
	for num in sorted:
		print(str(num))
	print()
	
print("Total Points: ", points)
	
#list = [1,2,3]
#list = [1,3,2]
#list = [2,1,3]
#list = [2,3,1]
#list = [3,1,2]
#list = [3,2,1]