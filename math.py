#import methods
import math
import sys
import os

#my math calculator made using python

#def clear
def clear():
	os.system('clear')

#while function true loop
while True:
	try:
		choice = input("1> addition\n2> multiplecation\n3> division\n4> square\n5> remainder\ntype stop to quit/exit\nchoice:" )

		#add numbers
		if choice == "1":
			clear()
			print("add")
			num1 = int(input("number to use: "))
			num2 = int(input("number to use: "))
			answer = num1 + num2
			print("answer: " + str(num1) + " + " + str(num2) + " = " + str(answer))
			print('-' * 20)

		#multiply numbers
		elif choice == "2":
			clear()
			print("multiply")
			num1 = int(input("number to use: "))
			num2 = int(input("number to use: "))
			answer = num1 * num2
			print("answer: " + str(num1) + " * " + str(num2) + " = " + str(answer))
			print('-' * 20)

		#devide numbers
		elif choice == "3":
			clear()
			print("devide")
			num1 = int(input("number to use: "))
			num2 = int(input("number to use: "))
			answer = num1 / num2
			print("answer: " + str(num1) + " / " + str(num2) + " = " + str(answer))
			print('-' * 20)

		#square number
		elif choice == "4":
			clear()
			print("square")
			num1 = int(input("number to use: "))
			num2 = int(input("number to use: "))
			answer = num1 ** num2
			print("answer: " + str(num1) + " ** " + str(num2) + " = " + str(answer))
			print('-' * 20)

		#remainder number
		elif choice == "5":
			clear()
			print("remainder")
			num1 = int(input("number to use: "))
			num2 = int(input("number to use: "))
			answer = num1 % num2
			print("answer: " + str(num1) + " % " + str(num2) + " = " + str(answer))
			print('-' * 20)

		#quit calculator
		elif choice == "stop".lower() or "stop".upper():
			sys.exit()

		else:
			pass
		

	#error handling
	except(ValueError):
		print("not valid input")
	

