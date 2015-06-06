
def puzzler_1(word):

    index = 0
    consecutive_dbl_ltr = 0
    
    while index < len(word)-1:
        current_char = word[index]
        next_char = word[index+1]
        if current_char == next_char:
            consecutive_dbl_ltr += 1
            index = index + 2
        else:
            consecutive_dbl_ltr = 0
            index += 1
        if consecutive_dbl_ltr == 3:
            return True
    #end while loop
    return False
# end puzzler_1 (word)

#print puzzler_1("ddeeff")
#print puzzler_1("pocahontas")
#print puzzler_1("abcddeeffghij")

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if puzzler_1(word):
        print word
