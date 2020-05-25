class Student:
	school_name = 'ucsc extension'
	def __init__(self, nm, ss, gpa, yr):
		self.name = nm
		self.ss = ss
		self.gpa = gpa
		self.yr = yr

	def get_name(self):
		return self.name
	@classmethod 
	def get_school_name(cls):
		return Student.school_name
	@staticmethod
	def calc_23():
		return 2+3
	def __str__(self):
		return "name = " + self.name + "; Social security=" + self.ss + "; GPA =" + str(self.gpa)

class Shape:
	def __init__(self):
		self.color = 'Blank'

	def get_color():
		return self.color

	def get_shape_type(self):
		return "Default"

class Triangle(Shape):
	def __init__(self, side_a, side_b, side_c):
		Shape.__init__(self)
		self.side_a = side_a
		self.side_b = side_b
		self.side_c = side_c

	def get_perimeter(self):
		return self.side_a + self.side_b + self.side_c

	def set_color(self, color):
		self.color = color

	def get_shape_type(self):
		return 'Triangle'

def main():
	print("This is main module")

if __name__ == "__main__":
	main()

print(dir(Student))
student1 = Student("George T", "123-45-6789", 3.3, 2020)
print(dir(student1))
print(student1.get_school_name())
print(Student.calc_23())
print(student1)

t = Triangle(3, 4, 5)
print(t.get_color())
print(t.get_shape_type())
print(t.get_perimeter())
