#!/usr/bin/env python3
# Kaushik Das

while True:
	stemp = input("Enter a temperature(number),or Ee to exit: ")
	if stemp in 'Ee' : break
	ftemp = float(stemp)
	
	sfrom = input("Enter FROM temperature unit:[Cc/Ff/Kk] ")
	if sfrom not in "CcFfKk" : continue
	sto = input("Enter TO temperature unit:[Cc/Ff/Kk] ")
	if sto not in "CcFfKk" : continue

	if sfrom in "Cc" and sto in "Kk":
		print("{0}C".format(ftemp + 273.15))
	elif sfrom in "Kk" and sto in "Cc":
		print("{0}K".format(ftemp - 273.15))
	elif sfrom in "Kk" and sto in "Ff":
		print("{0}F".format(ftemp * 9 / 5 - 459.67))
	elif sfrom in "Ff" and sto in "Kk":
		print("{0}K".format((ftemp + 459.67) * 5 / 9))
	elif sfrom in "Ff" and sto in "Cc":
		print("{0}C".format((ftemp - 32) * 5 / 9))
	elif sfrom in "Cc" and sto in "Ff":
		print("{0}F".format(ftemp * 9 / 5 + 32))
	else:
		print("Invalid From and To")
	