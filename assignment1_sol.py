greetings=\
'''
This is temperature conversion calculator
It converts from/to fahrenheit, celsious, and kelvin units.
'''
print(greetings)

while True:
	ans=input("Enter a temperature(number), or E to exit" )
	if len(ans) == 1 and ans[0] in "Ee":
		break; 

	temp = float(ans)

#process from temperature
	from_unit = input("Enter FROM temperature unit:[Cc/Ff/Kk] ")
	if len(from_unit) != 1:
		print(f"[ERROR] Invalid Temperature unit {from_unit} \nValid choices are:[Cc/Ff/Kk]\n")
		continue

	if from_unit not in  'CcFfKk':
		print(f"[ERROR] Invalid Temperature unit {from_unit} \nValid choices are:[Cc/Ff/Kk]\n")
		continue

#process to temperature
	to_unit = input("Enter TO temperature unit:[Cc/Ff/Kk] ")
	if len(to_unit) != 1:
		print(f"[ERROR] Invalid Temperature unit {to_unit} \nValid choices are:[Cc/Ff/Kk]\n")
		continue

	if to_unit not in  'CcFfKk':
		print(f"[ERROR] Invalid Temperature unit {to_unit} \nValid choices are:[Cc/Ff/Kk]\n")
		continue

#convert both temp units to upcase
	from_unit = from_unit.upper()
	to_unit = to_unit.upper()
	print(f"{temp}{from_unit} = {temp}{to_unit}\n")

	if from_unit == to_unit:
		new_temp = temp
	else:
		if from_unit == 'C':
			if to_unit == 'F':
				new_temp = temp * 1.8 + 32
			else:
				new_temp = temp + 273.15
		elif from_unit == 'F':
			if to_unit == 'C':
				new_temp = (temp - 32) / 1.8
			else:
				new_temp = (temp + 459.67) * 5 / 9
		else:
			if to_unit == 'C':
				new_temp = temp - 273.15
			else:
				new_temp = temp * 1.8 - 459.67

#print the results
	print(f"{temp}{from_unit} = {new_temp}{to_unit}\n")

