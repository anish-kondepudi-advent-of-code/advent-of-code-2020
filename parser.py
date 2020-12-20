file = open("C:/Users/Anish/Desktop/input.txt", "r")
for line in file:
	line = line.strip('\n')
	print(f"\"{line}\",")
file.close()