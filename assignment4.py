#!/usr/bin/env python3
# Kaushik Das
class Dog:
   total_nbr_of_dogs = 0
   breed_type_count = { }       #count of each known breed type encountered

   @classmethod
   def update_total(cls):
      #ADD CODE
      cls.total_nbr_of_dogs += 1

   @classmethod
   def get_total(cls):
      #ADD CODE
      return cls.total_nbr_of_dogs

   @classmethod
   def update_breed_count(cls, breed):
      #ADD CODE
      if breed in cls.breed_type_count.keys():
        cls.breed_type_count[breed] += 1
      else:
        cls.breed_type_count[breed] = 1

   @classmethod
   def print_breed_type_count(cls):
      field_sep = ' '*15
      header = 'Breed' + field_sep + 'Count'
      line = '='*len(header)
      #Note: the print below prints the 2 header lines in the output
      print(f"{header}\n{line}")
      #ADD CODE
      for b, c in cls.breed_type_count.items():
        print(b.ljust(23), c)

   def __init__(self, age, breed='UNKNOWN', name='*No Name*'):
      '''
         ADD CODE
         Note:
           age: a string of the following format: a positive_integer followed by a single character [Dd, Ww, Mm, Yy].
                Examples: '20h' (dog is 20 hours old), '5Y',(5 years old),  '6w' (6 Weeks) old
                No need to do any error checking for the validity of the age
           breed: a string. lower/upper/mixed cases should be considered the same. Example:'Great Dane' is same as 'great dane'
                If no breed is given, the dog's breed should be set to 'UNKNOWN'
           name: a string. The name is case sensitive, don't change it. Example: "Fido' and 'fido' would be different dog names
                if no name is given, the dog's name should be set to '*No Name*'
      '''
      self.age = age
      if breed=='UNKNOWN':
        self.breed = breed
      else:
        breed_f = breed.split()[0][:1:].upper() + breed.split()[0][1:].lower()
        if len(breed.split()) > 1:
          breed_l = breed.split()[1][:1:].upper() + breed.split()[1][1:].lower()
        else:
          breed_l = ""
        self.breed = breed_f + " " + breed_l
        self.update_breed_count(self.breed)  
      self.name = name
      self.update_total()
      
   def __str__(self):
      '''
         ADD CODE
         Override the __str__() so when print(dog) is called, it produces an output with following format:
         Name: dog's-name Age: dog's age exactly as displayed below Breed: First letter capitalized
         Name: Chewy    Age: 2Week(s)   Breed: Pitbull
      '''
      age_n = self.age[:-1:]
      age_u = self.age[-1:]
      if age_u == 'd' or age_u == 'D':
        age_us = 'Day'
      elif age_u == 'w' or age_u == 'W':
        age_us = 'Week'
      elif age_u == 'm' or age_u == 'M':
        age_us = 'Month'        
      elif age_u == 'y' or age_u == 'Y':
        age_us = 'Year'
      else:
        age_us = 'Hour'

      age_str = age_n + age_us
      if int(age_n) > 1:
        age_str += '(s)'
      return "Name: " + self.name.ljust(10) + "Age: " + age_str.ljust(12) + " Breed: " + self.breed

   def get_age(self):
      #ADD CODE
      return self.age

   def update_age(self, age):
      #ADD CODE
      #No need to do any error checking for 'age', assume it is valid
      self.age = age

#This is a helper function being called from main(). It is NOT member of class Dog
def update_dog_age_and_print(dog_list, name, age):
   #ADD CODE
   #Update the 'age' for the dog with the given 'name' in my dog list
   for d in dog_list:
    if d.name == name:
      d.update_age(age)
      print(f"\nNote: age was updated for: ", end = " ")
      print(d)

def main():
   '''
     ADD CODE to create the following 4 dogs:
      first dog:  Dog('2W', 'Pitbull', 'Chewy')
      second dog: Dog('3Y', 'Great Dane')
      third dog:  Dog('20D', 'PITBUll', 'Fido')
      fourth dog: Dog('2m')
   '''
my_dogs = []
my_dogs.append(Dog('2W', 'Pitbull', 'Chewy'))
my_dogs.append(Dog('3Y', 'Great Dane'))
my_dogs.append(Dog('20D', 'PITBUll', 'Fido'))
my_dogs.append(Dog('2m'))

Dog.print_breed_type_count()

print("\nTotal number of dogs: {}\n".format(Dog.get_total()))

#print the info about all my dogs
for d in my_dogs:
  print(d)

update_dog_age_and_print(my_dogs,'Chewy', '4w')

if __name__ == "__main__":
  main()