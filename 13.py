import tablib
def csv2xls(source,dest):
	'''returns an excel file by inputting a csv file'''
	data=tablib.Dataset()
	with open(source,'r') as f:
		data.csv=f.read()
	with open(dest,'wb') as f:
		f.write(data.xls)

import sys
source=sys.argv[1]
dest=sys.argv[2]
csv2xls(source,dest)
