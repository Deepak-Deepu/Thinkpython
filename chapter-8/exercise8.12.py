def rotate_word(word, num_shift):
    new_letter = ""
    new_word = ""
    word_lower = word.lower()
    
    for letter in word_lower:
        #rotate letter
        new_ltr_position = ord(letter)+num_shift
        
        # rotate z-->a or z<--a
        if new_ltr_position < ord('a'): #rotate z<--a
            new_ltr_position = new_ltr_position + 26
        elif new_ltr_position > ord('z'): #rotate z-->a
            new_ltr_position = new_ltr_position - 26
        
        #build new word
        new_letter = chr(new_ltr_position)
        new_word = new_word + new_letter

    return new_word

print rotate_word("melon",-10)
print rotate_word("cheer",7)
