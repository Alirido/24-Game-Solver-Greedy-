'''
Hello guys, jadi ini program saya untuk memecahkan 24 game solver.
Saya menggunakan strategi algoritma greedy
'''
from os import path as p
import operator

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
	f.close()
	return digits

def ito(x):
	if (x==5):
		return '+'
	elif (x==4):
		return '-'
	elif(x==3):
		return '*'
	else:
		return '/'

def get_operator_fn(op):
	return {
	'+' : operator.add,
	'-' : operator.sub,
	'*' : operator.mul,
	'/' : operator.div,
	'%' : operator.mod,
	'^' : operator.xor,
	}[op]

def eval_binary_expr(op1, oper1, op2, oper2, op3, oper3, op4):
	op1,op2,op3,op4 = int(op1), int(op2), int(op3), int(op4)
	return get_operator_fn(oper)(op1, op2)

def solve(arr): # USING GREEDY ALGORITHM
	sum = 15
	found = False
	while (sum>=6 and not found):
		# Generate all possible permutation of digits
		a = 5
		while (a>=2 and not found):
			b = 5
			while (b>=2 and not found):
				c = 5
				while (c>=2 and not found):
					ta = ito(a)
					tb = ito(b)
					tc = ito(c)
					return eval('arr[0] ta arr[1] tb arr[2] tc arr[3]')
		sum -= 1

def main():
	welcome()
	docum()
	c = input("Enter command: ")
	while not (c.lower() == 'q'):
		if (c.lower() == 'i'):
			digits = readFile()
			print("Jawabannya adalah: ")
			t1 = ito(5)
			t2 = ito(4)
			t3 = ito(3)
			print(eval_binary_expr("10 t1 20 t2 30 t3 40".split()))
			# print(solve(digits))
			# for num in digits:
			# 	print(num)
			print()
		elif c.lower() == 'd':
			docum()
		else:
			print("%s is invalid input." % c)
		c = input("Enter command: ")
	print("Thank you and see you later:)")

main()