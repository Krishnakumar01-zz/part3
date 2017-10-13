import re
import urllib
def links(url):
	'''returns all links in a webpage'''
	data=urllib.urlopen(url)
	print('\n'.join(re.findall(r'"http.*"',data.read())))

import sys
links(sys.argv[1])
