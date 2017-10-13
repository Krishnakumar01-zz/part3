import importlib
import inspect
import sys
def mydoc(module):
	'''returns module descriptipn and functions in it'''
	mo_dule=importlib.import_module(module)
	print('Module name is:'+module)
	print('Description: '+mo_dule.__doc__)
	a=dir(mo_dule)
	print(a)
	for i in a:
		inew=getattr(mo_dule,i)
		if inspect.isfunction(inew):
			print(i+'()')
		
	
mydoc(sys.argv[1])
