import re
def validate(number):
	'''returns if a mobile number is valid or not'''
	pattern=r'(^[1-9])([0-9]{9}$)'
	if re.match(pattern,number):
		print('Valid number')
	else:
		print('Invalid number')

import sys
validate(sys.argv[1])
