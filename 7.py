import re
def make_slug(word):
	'''returns the word with special characters replaced by -'''
	print(re.sub(r'^\W*','',re.sub(r'\W*$','',re.sub(r'\b\W*\b','-',word))))

make_slug('--hello!world@@')
