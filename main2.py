from itertools import permutations, product, zip_longest, chain
from fractions import Fraction as F

def readFile():
	f = open("test.txt")
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

def solveUsingGreedy(arr): # USING GREEDY ALGORITHM
	current_score = 0
	max_score = -10000
	ans = ''

	# permute all the digits
	arr_d = sorted(set(permutations(arr)))

	# All the bracket insertion points:
	brackets = ( [()] + [(x,y)
                         for x in range(0, 5, 2)
                         for y in range(x+4, 9, 2)
                         if (x,y) != (0,8)]
                 + [(0, 3+1, 4+2, 7+3)] ) # double brackets case

	# Open file to be wrote with the result
	output = open("output.txt", "w")

	# for bracket in brackets:
	for bracket in range(0, 7):
		if bracket == 0:
			min_score = 0
		elif bracket == 6:
			min_score = 2
		else:
			min_score = 1
		for op_score in range(16, 5, -1):
			for d in arr_d:

				for a in range(5, 1, -1):
					for b in range(5, 1, -1):
						for c in range(5, 1, -1):
							if (a+b+c > op_score):
								continue
							elif (a+b+c < op_score):
								break;
							else:
								ops = tuple((ito(a), ito(b), ito(c)))
								if (a==2 or b==2 or c==2):
									d2 = [('F(%s)' % i) for i in d]
								else:
									d2 = d
								exp = list(chain.from_iterable(zip_longest(d2, ops, fillvalue='')))

								# INSERTION OF BRACKET
								tid = 0
								count = 0
								op1 = -1
								op2 = -1
								op3 = -1
								for x in exp:
									if (x in "+-*/"):
										count += 1
										if count == 1:
											op1 = tid
										elif count == 2:
											op2 = tid
										elif count == 3:
											op3 = tid
									tid += 1
								last = tid
								if bracket == 1: 
									exp.insert(0, '(')
									exp.insert(op2+1, ')')
								elif bracket == 2:
									exp.insert(0, '(')
									exp.insert(op3+1, ')')
								elif bracket == 3:
									exp.insert(op1+1, '(')
									exp.insert(op3+1, ')')
								elif bracket == 4:
									exp.insert(op1+1, '(')
									exp.insert(last+1, ')')
								elif bracket == 5:
									exp.insert(op2+1, '(')
									exp.insert(last+1, ')')
								elif bracket == 6:
									exp.insert(0, '(')
									exp.insert(op2+1, ')')
									exp.insert(op3+1+2, '(')
									exp.insert(last+3, ')')

								# for insertpoint, br in zip(bracket, '()'*min_score):
								# 	exp.insert(insertpoint, br)

								txt = ''.join(exp)
								try:
									result = eval(txt)
								except ZeroDivisionError:
									break
								if result == 24:
									if '/' in ops:
										exp = [ (term if not term.startswith('F(') else term[2] if term[3]==')' else term[2]+term[3])
										for term in exp ]
									ans = ' '.join(exp).rstrip()
									output.write(ans)
									return ans
								else:
									current_score = a+b+c - min_score - abs(24 - result)
									if (current_score > max_score):
										max_score = current_score
										if '/' in ops:
											exp = [ (term if not term.startswith('F(') else term[2] if term[3]==')' else term[2]+term[3])
											for term in exp ]
										ans = ' '.join(exp).rstrip()
								break
	output.write(ans)
	output.close()

def main():
	digits = readFile()
	solveUsingGreedy(digits)

main()