class student:
	def details(self, name, age):
		self.name = name
		self.age = age
		print(f'My name is {self.name}')

a = student()
a.details("Tiya", 20)