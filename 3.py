import os
import time
def length(dirname):
	'''returns the file,size of the file,last modification time'''
	a=os.path.join('/home/krishnakumar/python/part3',dirname)
	for i in os.listdir(a):
		print(i),
		print('\t'),
		print(+os.stat(os.path.join(a,i)).st_size),
		print('\t'),
		print(time.ctime(os.stat(os.path.join(a,i)).st_mtime))

import sys
length(sys.argv[1])		
