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
	print("\td = Documentation")
	print("\tt = Testing\n")

def readFile():
	filename = input("Enter your input filename: ")
	while not p.exists(filename):
		print(filename, "file does not exists")
		filename = input("Enter your input filename: ")
	f = open(filename)
	data = f.readline()
	digits = data.split()
	f.close()
	return digits

def ito(x): # ito = Integer to Operator
	if (x==5):
		return '+'
	elif (x==4):
		return '-'
	elif(x==3):
		return '*'
	else:
		return '/'

def solve(arr): # USING GREEDY ALGORITHM
	score = 15
	found24 = False
	maks_score = -10000
	while (score>=6 and not found24):
		# Generate all possible permutation of digits
		a = 5
		while (a>=2 and not found24):
			b = 5
			while (b>=2 and not found24):
				c = 5
				while (c>=2 and not found24):
					if (a+b+c > score):
						continue
					elif (a+b+c == score):
						oa = ito(a)
						ob = ito(b)
						oc = ito(c)
						ans = "%d %c %d %c %d %c %d"
						ans = ans % (arr[0]. oa, arr[1], ob, arr[2], oc, arr[3])
						# if (eval(ans))
		score -= 1
					# return eval('arr[0] ta arr[1] tb arr[2] tc arr[3]')

def main():
	welcome()
	docum()
	c = input("Enter command: ")
	while not (c.lower() == 'q'):
		if (c.lower() == 'i'):
			digits = readFile()
			print("Jawabannya adalah: ")
			for num in digits:
				print(num)
			print()
		elif c.lower() == 'd':
			docum()
		elif c.lower() == 't':
			# FOR TESTING
			brackets = ( [()] + [(x,y)
                         for x in range(0, 7, 2)
                         for y in range(x+4, 7+2, 2)
                         if (x,y) != (0,7+1)]
                 + [(0, 3+1, 4+2, 7+3)] ) # double brackets case
			print("Brackets = ", end="")
			print(brackets)
		else:
			print("%s is invalid input." % c)
		c = input("Enter command: ")
	print("Thank you and see you later:)")

main()