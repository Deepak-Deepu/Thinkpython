a=3
b=4
c=5
n=2
def check_fermat(a, b, c ,n):
	if a**n + b**n == c**n:
		print('Holy smokes, Fermat was Wrong!')
	else:
		print('No, that doesn\'t work.')

print check_fermat(a,b,c,n)
