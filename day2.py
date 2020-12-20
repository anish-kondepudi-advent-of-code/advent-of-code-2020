# Tuple Containing Raw Data
password_tuple = ("1-3 a: abcde",
				"1-3 b: cdefg",
				"2-9 c: ccccccccc")

# Parses Data into Python List
password_list = []
for password in password_tuple:
	temp_list = []
	parsed_data = password.split(" ")
	parsed_range = parsed_data[0].split("-")
	temp_list.append(parsed_range[0])
	temp_list.append(parsed_range[1])
	temp_list.append(parsed_data[1][0])
	temp_list.append(parsed_data[2])
	password_list.append(temp_list)	

# Checks for Valid Passwords (Part 1)
total_passwords = len(password_list)
incorrect_passwords1 = 0
for password in password_list:
	if ((password[3].count(password[2]) < int(password[0])) or (password[3].count(password[2]) > int(password[1]))):
		incorrect_passwords1 += 1

# Checks for Valid Passwords (Part 2)
incorrect_passwords2 = 0
for password in password_list:
	if (password[3][int(password[0])-1] == password[2]) and (password[3][int(password[1])-1] == password[2]):
		incorrect_passwords2 += 1
	elif (password[3][int(password[0])-1] != password[2]) and (password[3][int(password[1])-1] != password[2]):
		incorrect_passwords2 += 1

# Prints Result for Part 1
print(total_passwords-incorrect_passwords1)

# Prints Result for Part 2
print(total_passwords-incorrect_passwords2)

