import zipfile
import os
def zipfiles(name,files):
	'''returns a zipfile with given file contents'''
	if name.split('.')[-1]=='zip':
		z_file=zipfile.ZipFile(name,'w',zipfile.ZIP_DEFLATED)
		for f in files:
			z_file.write(f)
		for i in z_file.namelist():
			print(i)

import sys
name=sys.argv[1]
files=sys.argv[2:]
zipfiles(name,files)
