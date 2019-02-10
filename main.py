'''
Hello guys, jadi ini program saya untuk memecahkan 24 game solver.
Saya menggunakan strategi algoritma greedy

Perintah:
q = Quit
i = Input
'''

def welcome():
	print(__doc__)
	print("Enter your input file: ")
	print("Untuk sementara input manual dulu aja disini: ")

def main():
	welcome()
	c = input("Enter command: ")
	while not (c.lower() == 'q'):
		print("Your input key is %c" % c)
		c = input("Enter command: ")
	print("Thank you and see you later:)")

main()