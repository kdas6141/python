import csv
#csv_file_name = 'data.csv'
csv_file_name = 'data_X.csv'
csv_file = open(csv_file_name)
print(f"CSV file: {csv_file_name}")
csv_file.readline()
#reader = csv.reader(csv_file)
reader = csv.reader(csv_file, delimiter='X', skipinitialspace=True)
for row in reader:
#	print(row)
	print('| '.join(row))
csv_file.close()

data_to_write = [
				 ["Full Name", "Marital Status", "Age"],
				 ["George Tool", "Married", 30],
				 ["Tim Duo", "Single", 45]
				]
csv.register_dialect('my_dialect', delimiter='|', quoting=csv.QUOTE_NONNUMERIC, quotechar='"')
csv_wfile_name = 'personal_info.csv'
csv_wfile = open(csv_wfile_name, 'w')
writer = csv.writer(csv_wfile, dialect='my_dialect')
#for row in data_to_write:
#	writer.writerow(row)
writer.writerows(data_to_write)
csv_wfile.close()


print("<<<<<<<<<<<<<<<<<<<CSV Dictionary Read>>>>>>>>>>>>>>>")
in_file=open('personal_info.csv')
reader = csv.DictReader(in_file)
for row in reader:
	for k in row.keys():
		print(f"{row[k]}")
	print('===if ===============')
for row in reader:
	if int(row['Age']) > oldest_age:
		oldest_age = int(row['Age'])
in_file.close()

print("<<<<<<<<<<<<<<<<<<<CSV Dictionary Write>>>>>>>>>>>>>>>")

field_names = ['Animal', 'Count']
inventory = [
				{'Animal':'cat', 'Count': 10},
				{'Animal':'dog', 'Count': 7},
				{'Animal':'dog fish', 'Count': 15},
			]

csv_wdfile = open('pets.csv', 'w')
writer = csv.DictWriter(csv_wdfile, fieldnames = field_names)
writer.writeheader()
writer.writerows(inventory)
csv_wdfile.close()

