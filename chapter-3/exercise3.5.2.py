def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def print_column():
	print '+ - - - - + - - - - + - - - - +'

def print_row():
	print '|         |         |         |'

def do_block():
	print_column()
	print_row()

def print_block():
	do_twice(do_block)
	print_column()

print print_block() 
