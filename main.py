'''
Hello guys, jadi ini program saya untuk memecahkan 24 game solver.
Saya menggunakan strategi algoritma greedy
'''

def welcome():
	print(__doc__)
	print("Enter your input file: ")
	print("Untuk sementara input manual dulu aja disini:")

def docum():
	print("\nList of commands: ")
	print("\tq = Quit")
	print("\ti = Input")
	print("\td = Documentation\n")

def main():
	welcome()
	docum()
	c = input("Enter command: ")
	while not (c.lower() == 'q'):
		if (c.lower() == 'i'):
			print("Your input key is %s" % c)
		elif c.lower() == 'd':
			docum()
		else:
			print("%s is invalid input." % c)
		c = input("Enter command: ")
	print("Thank you and see you later:)")

main()