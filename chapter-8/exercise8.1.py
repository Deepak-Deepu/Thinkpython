def backward_with_lines(word):
    index = len(word)
    while index > 0:
        print word[index-1]
        index = index -1

if __name__ == '__main__':
	print backward_with_lines('foo')
