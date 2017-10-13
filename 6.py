import urllib
import re
def antihtml(url):
	'''returns a webpage by removing all html tags'''
	data=urllib.urlopen(url)
        print(re.sub(r'<.*>',' ',data.read()))
	data.close()
	
import sys
antihtml(sys.argv[1])

