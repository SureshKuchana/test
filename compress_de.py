import collections

def count(str):
	str1 = str
	values = collections.Counter(str1)
	char_occured = {}

	for k,v in values.items():
		print(v,k,sep='',end='')
		if v > 1:
			char_occured[k] = v
	return ''
print(count("aaaabbcccccdde"))