import os
def count(dirname):
	"""returns the sorted list based on number of files in each extension"""
	a=os.listdir(os.path.join('/home/krishnakumar/python/part3',dirname))
	dicti={}
	for i in a:
		b=i.split('.')[-1]
		dicti[b]=dicti.get(b,0)+1
	d=dicti.items()
	d.sort(key=lambda x:x[-1])
	print(d)
	for i in d[::-1]:
		print(i[0]+' '+str(i[1]))

def main():
	import sys
	count(sys.argv[1])

if __name__=='__main__':
	main()
