import sys
import os
def print_twice(my_string):
	print my_string
	print my_string

def do_twice(f, num):
	f(num)
	f(num)

def do_four(f, num):
	do_twice(f, num)
	do_twice(f, num)

def main():
	do_four(print_twice, 'spam')

if __name__ == '__main__':
	main()














