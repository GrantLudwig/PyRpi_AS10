# File Name: ludwig_grant_AS10.py
# File Path: /home/ludwigg/Python/PyRpi_AS10/ludwig_grant_AS10.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS10/ludwig_grant_AS10.py

# Grant Ludwig
# 10/25/2019
# AS.10
# Sort 3 numbers

points = 0
    
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    
def bubbleSort(list):
    global points
    returnList = []
    for num in list:
        returnList.append(num)
    
    if returnList[0] > returnList[1]:
        swapPositions(returnList, 0, 1)
        points += 1
    points +=1
    if returnList[1] > returnList[2]:
        swapPositions(returnList, 1, 2)
        points += 1
    points +=1
    if returnList[0] > returnList[1]:
        swapPositions(returnList, 0, 1)
        points += 1
    points +=1
    
    return returnList

listOfList = ((1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1))

# bubble
print("Bubble Sort")
print("===========")
for list in listOfList:
	sorted = bubbleSort(list)
	for num in sorted:
		print(str(num))
	print()
    
print("Total Points: ", points)
points = 0
	
#list = [1,2,3]
#list = [1,3,2]
#list = [2,1,3]
#list = [2,3,1]
#list = [3,1,2]
#list = [3,2,1]