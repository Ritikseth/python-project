# import testing
# def do_stuff(num):
# 	try:
# 		if num and num!=0:
# 			return int(num) + 5
# 		elif num==0:
# 			return 'number can\'t be zero'
# 		else:
# 			return 'please enter a number'
# 	except ValueError as err:
# 		return err
from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)
# input from user?
# check that input is a number 1~10
def check_guess(check):
    if  0 < guess < 11 :
    	if guess == answer:
        	print('you are a genius!')
        	return True
      	else:
    	  	return 'wrong guess'
    else:
      	print('hey bozo, I said 1~10')
      	guess_number()

try:
	
