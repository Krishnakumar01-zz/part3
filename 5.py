import urllib
def printurl(url):
	'''Downloads and saves a page of the given url'''
	data=urllib.urlopen(url)
	if url[-1]=='/':
		print('saving'+url+'as index.html')
		f=open('index.html','w')
		f.write(data.read())
		f.close()
	else:
		print('saving '+url+' as '+url.split('/')[-1])
		f=open(url.split('/')[-1],'w')
		f.write(data.read())
		f.close()

import sys
printurl(sys.argv[1])
