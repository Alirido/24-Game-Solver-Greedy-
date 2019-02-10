'''
Hello guys, jadi ini program saya untuk memecahkan 24 game solver.
Saya menggunakan strategi algoritma greedy
'''
from os import path as p

def welcome():
	print(__doc__)
	print("Enter your input file: ")
	print("Untuk sementara input manual dulu aja disini:")

def docum():
	print("\nList of commands: ")
	print("\tq = Quit")
	print("\ti = Input")
	print("\td = Documentation\n")

def readFile():
	filename = input("Enter your input filename: ")
	while not p.exists(filename):
		print(filename, "file does not exists")
		filename = input("Enter your input filename: ")
	f = open(filename)
	data = f.readline()
	digits = data.split()
	return digits

def main():
	welcome()
	docum()
	c = input("Enter command: ")
	while not (c.lower() == 'q'):
		if (c.lower() == 'i'):
			digits = readFile()
			for num in digits:
				print(num)
			print()
		elif c.lower() == 'd':
			docum()
		else:
			print("%s is invalid input." % c)
		c = input("Enter command: ")
	print("Thank you and see you later:)")

main()