class Dog:
	total_nbr_of_dogs = 0
	breed_type_count = {}
	
	@classmethod
	def update_total(cls):
		cls.total_nbr_of_dogs += 1

	@classmethod
	def get_total(cls):
		return cls.total_nbr_of_dogs

	@classmethod
	def update_breed_count(cls, breed):
		breed = breed.upper()
		if breed not in cls.breed_type_count.keys():
			cls.breed_type_count[breed] = 1
		else:
			cls.breed_type_count[breed] += 1

	@classmethod
	def print_breed_type_count(cls):
		field_sep = ' '*15
		header = 'Breed' + field_sep + 'Count'
		line =  '=' * len(header)
		print(f"{header}\n{line}")
		for breed in cls.breed_type_count.keys():
			if breed.upper != 'UNKNOWN':
				print("{}{:5d}".format(breed.title().ljust(len('Breed')+len(field_sep)), cls.breed_type_count[breed]))

	def __init__(self, age, breed='UNKNOWN', name='*No Name*'):
		self.age = age.upper()
		self.breed = breed
		self.name = name
		Dog.update_total()
		Dog.update_breed_count(breed)

	def __str__(self):
		age_unit={'D':'Day(s)', 'W':'Week(s)', 'M':'Month(s)', 'Y':'Year(s)'}
		return "Name: " + self.name + "\tAge: " + self.age[0:len(self.age)-1] + age_unit[self.age[-1]] + "\tBreed: " + self.breed.title()

	def get_age(self):
		return self.age

	def update_age(self, age):
		self.age = age.upper()

def update_dog_age_and_print(dog_list, name, age):
	for d in dog_list:
		if d.name == name:
			d.update_age(age)
			print("\nNote: age was updated for: ", d)

def main():
#	dog1 = Dog('2W', 'Pitbull', 'Chewy')
#	dog2 = Dog('3Y', 'Great Dane')
#	dog3 = Dog('20D', 'PITBULL', 'Fido')
#	dog4 = Dog('2m')
#	my_dogs = [dog1, dog2, dog3, dog4]

	my_dogs = []
	my_dogs.append(Dog('2W', 'Pitbull', 'Chewy'))
	my_dogs.append(Dog('3Y', 'Great Dane'))
	my_dogs.append(Dog('20D', 'PITBUll', 'Fido'))
	my_dogs.append(Dog('2m'))

	Dog.print_breed_type_count()
	print(f"\nTotal number of dogs: {Dog.get_total()}")
	for d in my_dogs:
		print(d)

	update_dog_age_and_print(my_dogs, 'Chewy', '4w')

if __name__ == "__main__":
	main()
