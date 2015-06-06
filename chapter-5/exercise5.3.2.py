a=int(raw_input('Whay value to use for a?\n'))
b=int(raw_input('Whay value to use for b?\n'))
c=int(raw_input('Whay value to use for c?\n'))
n=int(raw_input('Whay value to use for n?\n'))

def check_fermat(a,b,c,n):
	if a**n + b**n == c**n:
		print('Holy smokes,Fermat was Wrong!')
	else:
		print('No, That doesn\'t work.')

print check_fermat(a,b,c,n)
