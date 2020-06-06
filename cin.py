import re 

def cin(str):
	print("Given CIN is : " + str)
	temp = re.match("([a-zA-Z]+)([0-9]+)([a-zA-Z]+)([0-9]+)([a-zA-Z]+)([0-9]+)",str,re.I) 
	values = temp.groups()
	keys = ('Listing status','Industry Type','State','Company incorporate year','Company Type','Registration Number')
	d = dict(zip(keys,values))
	print(d)
cin("U74999HR2014PTC053030")
