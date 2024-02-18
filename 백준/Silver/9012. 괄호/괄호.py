import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	while '()' in v:
		v = v.replace('()', '')
	
	if v:
		print('NO')
	else:
		print('YES')