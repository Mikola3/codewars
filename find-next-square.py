'''
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''

def find_next_square(sq):
    root = sq**0.5
    if root.is_integer() == True:
        return int((root+1)**2)
    else:
        return -1

print("---Beteer-Solution---")
'''
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return int(root + 1)**2
    return -1
'''
