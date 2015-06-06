def eval_loop():
	while True:
        	user_string = raw_input('>>> ')
        	if user_string == 'done':
            		break
        	else:
            		print user_string
            		result = eval(user_string)
           		print result

if __name__ == '__main__':
    eval_loop()
