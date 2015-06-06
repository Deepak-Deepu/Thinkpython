def is_anagram(t,u):
    if sorted(t)== sorted (u):
        return True
    else:
        return False


print is_anagram('realtor', 'rotlear')
