
# Reads Raw Data from input.txt file
rawData = list()
file = open("C:/Users/Anish/Desktop/input.txt", "r")
for line in file:
	line = line.strip('\n')
	rawData.append(line)
file.close()

parsedData = list()
subList = list()
for line in rawData:
	if line == "":
		parsedData.append(subList)
		subList.clear()
		continue
	subList.append(line)


print(parsedData)

